# graphql-to-rest-example

Example of making a REST API compatible with GraphQL

# Set up

## Requirements

* Install docker-compose and docker (or figure out how to run everything without)

## Run

`make run` 

* spins up a flask app running on `localhost:5000`
* listens for graphql POST requests on `localhost:5000/graphql`

## Test

`make test` (uses pytest)

## Modify

* The file you want to change is `schema.py`
* GraphQL has some nuances you must conform to. Ex: 
  * Sometimes you have to use camelcase in requests
  * IDs are returned as strings, regardless of whether the REST endpoint gave integers
