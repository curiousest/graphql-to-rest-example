FROM python:3.5.3-alpine

RUN pip3 install pytest-flask==0.10.0 \
    Flask==0.12.2 \
    Flask-GraphQL==1.4.1 \
    requests==2.9.1 \
    requests-mock==1.3.0 \
    graphene==1.4 \
    graphql-core==1.1 \
    graphql-relay==0.4.5 \
    graphql-to-rest==1.0 \
    pytest==3.1.2 \
    pytest-flask==0.10.0

ADD ./src /code/

WORKDIR /code/graphql_to_rest_server

CMD python /code/graphql_to_rest_server/app.py
