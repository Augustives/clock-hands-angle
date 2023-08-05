# Django Clock Hands Angle API

## Setup:
- Create a virtual env with python, `python -m venv venv`
- Activate the virtual env
- Install the requirements, `pip install -r requirements.txt`
 
## Commands:
*Make sure you have docker installed and running*
- Run `make up` in the root folder of the project to build and start the container
- Run `make down` in the root folder of the project to stop the container
- Run `make rm` in the root folder of the project to remove the container
- Run `make test` in the root folder of the project to run the tests

## Urls and User:
- Django will be available on `localhost:8000`
- Django admin user and password are "admin"

## Calculating an angle:
To calculate an angle make a get request to `localhost:8000/clock-angle/<hours>/<minutes>`, you can use Postman to make the requests
- Always returns the rounded down smaller angle between the clock hands
- Requests with the same parameters are retrieved from the database instead of calculated
- Hours are ints between 0 and 24
- Minutes are ints between 0 and 59
- There is no need to send minutes if you dont want to
- Database already has some angles calculated, they are inserted through fixtures when you build the project

<br>

GET: `localhost:8000/clock-angle/6/`
```
{
    "angle": 180
}
```