## Getting Started
The product is built on the following stack:

* Python 3.8
* PostgreSQL 11
* Docker

Ensure you have Docker, docker-compose and Make installed and running prior to the steps that follow.

## Installing

- Run the commands below in your terminal to clone and setup the project

```shell
# clone the project
$ git clone https://github.com/BarnaTB/postcodes.git

# open the project directory
$ cd postcodes
```

- Create a `.env` file your current directory
- Copy the contents of the `.env.example` file and paste it in your `.env` file and follow the comments in there to set up the required environment variables

- Navigate to the django-admin interface by visiting http://localhost:8000/admin/ in your browser and login with the credentials you just created
- Click the `Listings` model in left nav bar adjuscent ot the `Add` button, click `Upload a csv` to upload a csv of your listings data

- Using your api client of choice, hit the following endpoints both with `GET` requests.

`api/outcode/{outcode}`

`api/nexus/{outcode}`

where `outcode` is the first part of the UK postal code e.g M11

## Running the tests
Run the tests by running `make test` or `make test APP=<insert-app-name>` to run app specific tests

## To-do

The tasks below are still pending.
- Appropriate API documentation
- CI/CD
- Deployment to a cloud PaaS(Heroku, or Digital Ocean)

## Acknowledgement

Many thanks to the team at [Pass The Keys](https://passthekeys.co.uk/) for all the support on the project
