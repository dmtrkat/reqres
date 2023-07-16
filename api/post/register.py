import requests as r
from rootpackage.base import Base


class Register:
    base = Base()
    data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = {"id": 4, "token": "QpwL5tke4Pnpja7X4"}

    def test_register(self):

        """Шаги:
        0. Отправить POST-запрос
        1. Проверить статус-код. Должен быть 200
        2. Конвертировать данные в json
        3. Убедиться, что юзер создан"""

        response = r.post(self.base.API_CONSTANTS.POST.post_register(), data=self.data)
        if response.status_code == self.base.API_CONSTANTS.STATUS200:
            json = response.json()
            id_response = json.get("id")
            token_response = json.get("token")
            assert self.response.get("id") == id_response and self.response.get("token") == token_response
            print("Тест пройден!")
        else:
            print("Ошибка, статус " + str(response.status_code))


create = Register()
create.test_register()
