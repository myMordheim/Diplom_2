import requests
import allure
from faker import Faker
from endpoints import Endpoints


class Helper:
    @staticmethod
    def generate_user_data():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        reg_data = {
            "email": email,
            "password": password,
            "name": name
        }
        return reg_data

    @allure.step('Пользователь регистрируется')
    def register(self):
        payload = Helper.generate_user_data()
        return requests.post(Endpoints.create_user, data=payload)

    @staticmethod
    def delete_user():
        return requests.delete(Endpoints.delete_user)
