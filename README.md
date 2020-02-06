# happy-birthday-flask
Simple flask app for birthday wishes! It checks for valid username input (only letters) and for duplicates and returns birthday wishes!


### Endpoints
Following are the endpoints are implemented

| Name   | Method      | URL
| ---    | ---         | ---
| List   | `GET`       | `/hello`
| Create | `POST`      | `/hello/{name`
| Get    | `GET`       | `/hello/{name}`
| Update | `PUT/PATCH` | `/hello/{name}`

# Usage

**To run e2e and unit test:**
```sh
pipenv install; pipenv run pytest tests
```

**To launch in docker:**
```sh
export SERVE_PORT=9000
export ENVIRONMENT=development
./docker_launch.sh
```
