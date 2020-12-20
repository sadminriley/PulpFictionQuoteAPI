#!/usr/bin/env python3

from flask import Flask, jsonify, request
from json import dumps
from flask_restful import Resource, Api
import sqlalchemy


app = Flask(__name__)
pulpapi = Api(app)

# Load quotes from sqlite database
db = sqlalchemy.create_engine('sqlite:///quote.db')


class PulpResource(Resource):
    '''Flask Resource with database connection'''

    def __init__(self):
        '''init db'''
        self.db = db.connect()

    def query_to_json(self, key='result', query=''):
        result = {key: [dict(row) for row in self.db.execute(query)]}
        return jsonify(result)


class Health(PulpResource):
    '''
    [GET] / - Returns 200 for health check because AWS is a pain in my ass
    '''
    def get(self):
        return 'Healthy!'


class Characters(PulpResource):
    '''
    [GET] Character - Pulp Fiction Movie Characters
    '''

    def get(self):
        '''
        List all tables for each character
        '''
        query = self.db.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = {'Available Characters': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Quote(PulpResource):
    '''
    [GET, POST] Quote - Pulp Fiction Movie Quotes
    '''

    def get(self, name):
        '''
        List random quote from passed character
        '''
        query = f"SELECT * FROM {name} ORDER BY RANDOM() LIMIT 1;"
        return self.query_to_json(f"{name} says...", query)

    def post(self, name):
        '''
        Inserts a quote into the database
        '''
        self.db.execute(f"INSERT INTO {name} VALUES('{request.form['quote']}');")
        return jsonify({'status': 'success'})


# Routing
pulpapi.add_resource(Health, '/')
pulpapi.add_resource(Characters, '/characters')
pulpapi.add_resource(Quote, '/quote/<name>')


if __name__ == '__main__':
    '''
    No port/host  neccessary since the docker launch specificies it.
    '''
    app.run(host='0.0.0.0')
