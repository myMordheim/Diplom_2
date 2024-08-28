import pytest
from helper import *
import requests

@pytest.fixture(scope="function")
@allure.title("Создания пользователя для теста и удаление его по заверешению")
def user_create_for_test():
    payload = Helper.generate_user_data()
    response = requests.post(Endpoints.create_user, data=payload)
    yield payload, response
    requests.delete(Endpoints.user_data, headers={"Authorization": response.json()["accessToken"]})