import json
from http import HTTPStatus

import pytest

def test_post_user(session, test_client, sample_post_data1):
## Testing POST
    response = test_client.post(
        '/hello/bob',
        data=json.dumps(sample_post_data1),
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.CREATED

## Testing GET
    response = test_client.get('/hello/bob')
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.OK

## Testing POST for user that already exists
    response = test_client.post(
        '/hello/bob',
        data=json.dumps(sample_post_data1),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_happy_birthday(session, test_client, sample_happy_birthday):
## Testing POST again
    response = test_client.post(
        '/hello/sally',
        data=json.dumps(sample_happy_birthday),
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.CREATED

## Testing GET happy birthday!
    response = test_client.get('/hello/sally')
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert 'Happy Birthday' in response_data

def test_bad_input(session, test_client, sample_post_data1):
## Testing bad input with numbers
    response = test_client.post(
        '/hello/num923720',
        data=json.dumps(sample_post_data1),
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_put_user(session, test_client, sample_post_data1):
## Testing PUT again
    response = test_client.put(
        '/hello/bob',
        data=json.dumps(sample_post_data1),
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.CREATED
## Testing put with bad input
    response = test_client.put(
        '/hello/num923720',
        data=json.dumps(sample_post_data1),
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST