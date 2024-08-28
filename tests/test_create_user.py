import allure
from helper import Helper
from endpoints import *
import pytest
import requests
from data import *

class TestCreateUser:

    @allure.title('создать уникального пользователя')
    def test_create_user(self):
        response = requests.post(Endpoints.create_user, data=Helper.generate_user_data())
        assert response.json()["success"] is True and response.status_code == 200

    @allure.title('создать пользователя, который уже зарегистрирован')
    def test_create_user_already_registered(self):
        requests.post(Endpoints.create_user, data=Data.data_user_for_double)
        response = requests.post(Endpoints.create_user, data=Data.data_user_for_double)
        assert response.json()["success"] is False and response.status_code == 403 and response.json()["message"] == EndpointsMessageText.double_user

    @allure.title('создать пользователя и не заполнить одно из обязательных полей.')
    @pytest.mark.parametrize("incorrect_data", Data.data_for_registr_parametrize)
    def test_create_user_without_one_input(self, incorrect_data):
        response = requests.post(Endpoints.create_user, data=incorrect_data)
        assert response.json()["success"] is False and response.status_code == 403 and response.json()["message"] == EndpointsMessageText.without_one_input