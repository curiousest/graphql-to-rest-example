SHELL := /bin/bash

run:
	docker-compose run graphql-to-rest

run_debug:
	docker-compose run export FLASK_DEBUG=1 && flask run

test:
	docker-compose run graphql-to-rest python -m pytest --capture=no

build:
	docker-compose build graphql-to-rest
