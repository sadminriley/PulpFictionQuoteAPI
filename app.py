#!/usr/bin/env python

from flask import Flask, jsonify, request
from json import dumps
from flask_restful import Resource, Api
import sqlalchemy


app = Flask(__name__)
pulpapi = Api(app)

# Load quotes from sqlite database
db = sqlalchemy.create_engine('sqlite:///quote.db')


class Character(Resource):
    def get(self):
        conn = db.connect()
        # List all tables for each character
        query = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = {'Available Characters': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Quote(Resource):
    def get(self, character_quote):
        conn = db.connect()
        # List random quote from passed character
        query = conn.execute("SELECT * FROM %s ORDER BY RANDOM() LIMIT 1;" % (character_quote))
        result = {f"{character_quote} says...": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


pulpapi.add_resource(Character, '/character')  # Route 1
pulpapi.add_resource(Quote, '/character/<character_quote>')  # Route 2


if __name__ == '__main__':
    '''
    No port/host  neccessary since the docker launch specificies it.
    '''
    app.run(host='0.0.0.0')
