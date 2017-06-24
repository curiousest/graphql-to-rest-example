FROM python:3.5.3-alpine

RUN pip3 install pytest-flask==0.10.0 \
    Flask==0.12.2 \
    Flask-GraphQL==1.4.1 \
    requests==2.9.1 \
    requests-mock==1.3.0 \
    graphene==1.4 \
    graphql-core==1.1 \
    graphql-relay==0.4.5

ADD ./src /code/

RUN export FLASK_APP=/code/app.py

WORKDIR /code/
