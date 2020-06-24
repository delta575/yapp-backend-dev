import json

import pytest

from yapp_backend import app as api


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


def test_movie_list_handler(apigw_event, mocker):
    event_mods = dict(
        body=dict(),
        pathParameters=dict(),
        queryStringParameters=dict(),
        httpMethod="GET",
    )
    apigw_event.update(event_mods)

    ret = api.movie_list_handler(apigw_event, "")
    body = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "data" in body
    assert len(body["data"]) > 0
    assert "id" in body["data"][0]


def test_movie_get_handler(apigw_event, mocker):
    event_mods = dict(
        body=dict(),
        pathParameters=dict(id=158),
        queryStringParameters=dict(),
        httpMethod="GET",
    )
    apigw_event.update(event_mods)

    ret = api.movie_get_handler(apigw_event, "")
    body = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "data" in body
    assert "id" in body["data"]


def test_movie_create_handler(apigw_event, mocker):
    event_mods = dict(
        body=json.dumps(dict(title="Create Movie Test Ok")),
        pathParameters=dict(),
        queryStringParameters=dict(),
        httpMethod="POST",
    )
    apigw_event.update(event_mods)

    ret = api.movie_create_handler(apigw_event, "")
    body = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "data" in body
    assert "id" in body["data"]
    assert body["data"]["title"] == "Create Movie Test Ok"


def test_movie_update_handler(apigw_event, mocker):
    event_mods = dict(
        body=json.dumps(dict(id=3, title="PUT Test Ok")),
        pathParameters=dict(),
        queryStringParameters=dict(),
        httpMethod="PUT",
    )
    apigw_event.update(event_mods)

    ret = api.movie_update_handler(apigw_event, "")
    body = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "data" in body
    assert "id" in body["data"]
    assert body["data"]["title"] == "PUT Test Ok"


def test_movie_delete_handler(apigw_event, mocker):
    event_mods = dict(
        body=dict(),
        pathParameters=dict(),
        queryStringParameters=dict(id=5),
        httpMethod="DELETE",
    )
    apigw_event.update(event_mods)

    ret = api.movie_delete_handler(apigw_event, "")

    assert ret["statusCode"] == 200
    assert "body" not in ret
