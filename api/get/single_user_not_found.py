import requests as r
from rootpackage.base import Base


class SingleUserNotFound:

    base = Base()
    empty_dict = {}

    def test_single_user_not_found(self):
        """Шаги:
        1. Отправить GET-запрос
        2. Проверить статус-код. Должен быть 404
        3. Убедиться, что юзер не найден"""

        response = r.get(self.base.API_CONSTANTS.GET.get_single_user_not_found())
        if response.status_code == self.base.API_CONSTANTS.STATUS404:
            response = response.json()
            assert response == self.empty_dict
            assert len(response) == 0
            print("Тест пройден!")
        else:
            print("Ошибка: " + str(response.status_code))

single = SingleUserNotFound()
single.test_single_user_not_found()