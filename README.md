# Graphene Simac Backend

## About

This repository serves as the backend of the Simac application. It is setup by using Django + GraphQL to make an API with the help of the Graphene library/module.

## Requirements
* Python V3.+

## Installation

```
git clone https://github.com/YassinAO/graphene_simac_backend
cd graphene_simac_backend
pip install pipenv 
pipenv shell
pip install -r requirements.txt
copy .env-boilerplate .env
```
#### **Make sure to change the credentials in the .env file to fit your needs.**


Once you have the database up and running, use the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
To run the server use the command:
```
python manage.py runserver
```
To make use of graphiql in development navigate to:
127.0.0.1:8000/graphql
or
localhost:8000/graphql
