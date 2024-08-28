from URL import Url


class Endpoints:
    get_ingretients = f'{Url.main}/api/ingredients'  # получение данных об ингредиентах
    create_order = f'{Url.main}/api/orders'  # создание заказа
    password_reset = f'{Url.main}/api/password-reset'  # Восстановление и сброс пароля
    create_user = f'{Url.main}/api/auth/register'  # Создание пользователя
    login = f'{Url.main}/api/auth/login'  # эндпоинт для авторизации
    logout = f'{Url.main}/api/auth/logout'  # эндпоинт для выхода из системы
    user_data = f'{Url.main}/api/auth/user'  # эндпоинт для получения и обновления данных о пользователе
    delete_user = f'{Url.main}/api/auth/user'  # Удаление пользователя
    get_orders = f'{Url.main}/api/orders/all'  # Получить все заказы (Максимум 50 заказов)
    get_order = f'{Url.main}/api/orders'  # Получить заказы конкретного пользователя


class EndpointsMessageText:
    double_user = "User already exists"
    without_one_input = "Email, password and name are required fields"
    wrong_cred_login = "email or password are incorrect"
