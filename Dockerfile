FROM python:3.11-alpine

MAINTAINER sadminriley

ADD app.py /

ADD quote.db /

ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
