SHELL := /bin/bash

run:
	export FLASK_APP=src/app.py
	flask run

run_debug:
	export FLASK_DEBUG=1
	run

test:
	py.test --capture=no

build:
	dc build graphql-to-rest
