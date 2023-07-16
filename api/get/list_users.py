import requests as r
from rootpackage.base import Base


class ListUser:
    base = Base()

    def test_list_user(self):
        """Шаги:
        0. Отправить GET-запрос
        1. Проверить статус-код. Должен быть 200
        2. Конвертировать данные в формат json
        3. Ассерт, что данные из json доступны и заполнены (что API живое)
        4. Ассерт, что в списке (словаре) не один юзер, а больше"""

        response = r.get(self.base.API_CONSTANTS.GET.get_list_users(1))
        if response.status_code == self.base.API_CONSTANTS.STATUS200:
            json = response.json()
            for i in json.get("data"):
                assert i.get("id") is not None
                assert i.get("email") is not None
                assert i.get("first_name") is not None
                assert i.get("last_name") is not None
                assert i.get("avatar") is not None
                self.base.requests
            assert len(json) > 1
            print("Тест пройден!")



l = ListUser()
l.test_list_user()
