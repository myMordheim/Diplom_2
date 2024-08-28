import allure
from conftest import *
from helper import Helper
from endpoints import *
import pytest
import requests
from data import *

class TestGetOrders:

    def test_get_order_auth(self, user_create_for_test):
        token = user_create_for_test[1].json()["accessToken"]
        requests.post(Endpoints.login, data=user_create_for_test[0])
        response = requests.get(Endpoints.get_orders, headers={"Authorization": token})
        assert response.json()["success"] is True and response.status_code == 200

    def test_get_order_negative_auth(self):
        response = requests.get(Endpoints.get_orders)
        assert response.status_code == 401