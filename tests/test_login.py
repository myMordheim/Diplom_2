import allure
from conftest import *
from helper import Helper
from endpoints import *
import pytest
import requests
from data import *

class TestLoginUser:

    @allure.title('логин с валидными кредами')
    def test_login_user(self, user_create_for_test):
        response = requests.post(Endpoints.login, data=user_create_for_test[0])
        assert response.json()["success"] is True and response.status_code == 200

    @allure.title('логин с неверными кредами,')
    def test_incorrect_cred(self):
        response = requests.post(Endpoints.login, data=Helper.generate_user_data())
        assert response.json()["success"] is False and response.status_code == 401 and response.json()["message"] == EndpointsMessageText.wrong_cred_login