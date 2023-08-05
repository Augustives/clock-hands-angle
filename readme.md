# Django Clock Hands Angle API

## Commands:
    *Make sure you have docker installed and running.*
    - Run `make up` in the root folder of the project to build and start the container.
    - Run `make down` in the root folder of the project to stop the container.
    - Run `make rm` in the root folder of the project to remove the container and related images and volumes.
    - Run `make test` in the root folder of the project to run the tests.

## Urls and User:
    - Django will be available on `localhost:8000`
    - Django admin user and password are "admin"

## Calculating an angle:
To calculate an angle make a get request to `localhost:8000/clock-angle/<hours>/<minutes>`.
    - Always returns the rounded down smaller angle between the clock hands.
    - Requests with the same parameters are retrieved from the database instead of calculated.
    - Hours are ints between 0 and 24
    - Minutes are ints between 0 and 59
    - There is no need to send minutes if you dont want to.


GET: `localhost:8000/clock-angle/6/`
```
{
    "angle": 180
}
```