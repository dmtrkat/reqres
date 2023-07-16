class ApiConstants:

    def __init__(self):
        self._get = self.GET
        self._post = self.POST
        self._URL = self._URL

    # Статус коды
    STATUS200 = 200
    STATUS201 = 201
    STATUS404 = 404

    # Базовый URL
    _URL = "https://reqres.in"

    class GET:

        @staticmethod
        def get_list_users(page_number) -> str:
            """Список пользователей. Статус 200"""
            return ApiConstants._URL + f"/api/users?page={page_number}"

        @staticmethod
        def get_single_user_not_found():
            """Юзер не найден. Ошибка 404"""
            return ApiConstants._URL + "/api/users/23"

    class POST:

        @staticmethod
        def post_create():
            """Создание пользователей. Статус 201"""
            return ApiConstants._URL + "/api/users"

        @staticmethod
        def post_register():
            """Регистрация пользователя. Статус 200"""
            return ApiConstants._URL + "/api/register"
