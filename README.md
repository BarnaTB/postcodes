## Getting Started
The product is built on the following stack:

* Python 3.8
* Celery
* RabbitMQ
* PostgreSQL
* Virtualenv

Ensure you have Docker and Make installed and running prior to the steps that follow.

## Installing

Run the commands below in your terminal to clone and setup the project

```shell
# clone the project
$ git clone https://github.com/BarnaTB/product-importer.git

# open the project directory
$ cd product-importer

# checkout to this branch
$ git checkout dockerize-backend-service

# build the project and all its dependencies
$ make build

# run the application
$ make up
```

The project should be ready to run now so run `python manage.py runserver` and hit the endpoints according to the [documentation here](https://fulfilproductimporter.herokuapp.com/api/v1/docs/).

## Running the tests
Run the tests by running `make test` or `make test APP=<insert-app-name>` to run app specific tests
