import allure
from conftest import *
from helper import Helper
from endpoints import *
import pytest
import requests
from data import *

class TestOrders:

    def test_create_order_auth(self, user_create_for_test):
        token = user_create_for_test[1].json()["accessToken"]
        requests.post(Endpoints.login, data=user_create_for_test[0])
        response = requests.post(Endpoints.create_order, headers={"Authorization": token}, data=Data.data_ingridients)
        assert response.json()["success"] is True and response.status_code == 200

    def test_create_order_negative_auth(self):
        response = requests.post(Endpoints.create_order, data=Data.data_ingridients)
        assert response.status_code == 200

    def test_create_order_without_ingridients(self, user_create_for_test):
        token = user_create_for_test[1].json()["accessToken"]
        requests.post(Endpoints.login, data=user_create_for_test[0])
        response = requests.post(Endpoints.create_order, headers={"Authorization": token}, data={})
        assert response.json()["success"] is False and response.status_code == 400

    def test_create_order_negative_hash(self, user_create_for_test):
        token = user_create_for_test[1].json()["accessToken"]
        requests.post(Endpoints.login, data=user_create_for_test[0])
        response = requests.post(Endpoints.create_order, headers={"Authorization": token}, data=Data.data_ingridients_negative_hash)
        assert response.status_code == 500

