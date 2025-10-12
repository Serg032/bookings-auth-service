import os
import httpx
from behave import given, when, then
import logging

logger = logging.getLogger(__name__)

BASE_URL = os.getenv("API_URL_ATEST", "http://localhost:8000")


@given('a fresh username "{username}"')
def step_impl(context, username):
    context.username = username
    logger.info(f"Username set to: {context.username}")


@when("I update via PUT /update/{test_id}")
def step_impl(context, test_id):
    logger.info(f"Updating user with test_id: {test_id}")
    # payload = {"username": context.username}

    with httpx.Client(base_url=BASE_URL, timeout=5.0) as client:
        context.response = client.put(f"/update/test_id")


# @then("the response should be successful")
# def step_impl(context):
#     assert (
#         context.response.status_code == 200
#     ), f"Expected status 200, got {context.response.status_code}"
#     logger.info("Update request completed successfully")
