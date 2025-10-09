FROM python:3.14.0-alpine

MAINTAINER sadminriley

ADD app.py /

ADD quote.db /

ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
