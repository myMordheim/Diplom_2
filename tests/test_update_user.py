import allure
from conftest import *
from helper import Helper
from endpoints import *
import pytest
import requests
from data import *

class TestUpdateUser:

    @allure.title('Обновить данные пользователя')
    def test_user_update(self, user_create_for_test):
        token = user_create_for_test[1].json()["accessToken"]
        requests.post(Endpoints.login, data=user_create_for_test[0])
        response = requests.patch(Endpoints.user_data, headers={"Authorization": token}, data=Helper.generate_user_data())
        assert response.json()["success"] is True and response.status_code == 200

    @allure.title('Обновить даннные пользователя без авторизации')
    def test_user_update_negative(self, user_create_for_test):
        requests.post(Endpoints.login, data=user_create_for_test[0])
        response = requests.patch(Endpoints.user_data, data=Helper.generate_user_data())
        assert response.json()["success"] is False and response.status_code == 401