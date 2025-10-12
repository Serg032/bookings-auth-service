import os
import httpx
from behave import given, when, then

BASE_URL = os.getenv("API_URL_ATEST", "http://localhost:8000")


@given('a fresh username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.username = username
    context.password = password


@when("I register via POST /register")
def step_impl(context):
    payload = {"username": context.username, "password": context.password}
    with httpx.Client(base_url=BASE_URL, timeout=5.0) as client:
        context.response = client.post("/register", json=payload)


@then("the response status should be {status:d}")
def step_impl(context, status):
    assert context.response.status_code == status, context.response.text


@then('the response should contain fields "id" and "access_token"')
def step_impl(context):
    data = context.response.json()
    assert "id" in data and data["id"], "missing id"
    assert "access_token" in data and data["access_token"], "missing access_token"


@then('the response "username" should equal "{expected}"')
def step_impl(context, expected):
    data = context.response.json()
    assert data.get("username") == expected, data


@then('the response error detail should be "{message}"')
def step_impl(context, message):
    data = context.response.json()
    assert data.get("detail") == message, data
