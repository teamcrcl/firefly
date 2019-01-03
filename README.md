# Internship Challenge

## Prerequisites
- The project that you'll be using is a REST API, so if you don't know what that means familiarize yourself with the concept of REST.
- The task also assumes that you're familiar with git and github - You don't need to be a ninja, just some basic understanding should get you through.
- Finally the project uses the most popular python framework - django. Knowing your way around django will be helpful, but not necessary as you'll be doing that as part of the task.

This is the simplest REST API you'll ever come across in your professional career, however it's still is a full django app. We'll be using this code base to test your suitability for the internship.

## Set up

- Clone the project.
- cd into the project root.
- Creat a virtual env: `python3 -m venv env`
- Activate it: `source env/bin/activate`
- Install the dependencies: `pip3 install requirements.txt`
- Run migrations `./manage.py migrate`
- This will create SQLite the database with the necessary schema.
- Now that you've the database set up, let's fetch the data. `./manage.py fetch_countries`
- This will populate your database with the countries of the world. It's a django management command and the implementation can be found in countries>management>commands>fetch_countries 

## Tasks
- Familiarize yourself with django and the code flow in the project. You'll rarely ever write code from scratch in the real world. It's an important software engineering skill to get familiar with a code base quickly.
- The project exposes one endpoint - `http://127.0.0.1:8000/v1/fetch/countries` Try out the endpint in POSTMAN and convince yourself that it's a list of countries in JSON format. Knowing POSTMAN is an invaluable skill if you're working with REST APIs. It's a simple yet very powerful tool.
- Create a branch with your name, separated by -: `git checkout -b firstname-lastname`
- Write a set of unit tests and integration tests for the project - write as many tests as you wish, the aim is to see what are you testing and how.

