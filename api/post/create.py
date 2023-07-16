import requests as r

from rootpackage.base import Base


class Create:
    base = Base()
    data = {"name": "morpehus", "job": "leader"}
    response = {"name": "morpehus", "job": "leader"}

    def test_create(self):
        """Шаги:
        0. Отправить POST-запрос
        1. Проверить статус-код. Должен быть 201
        2. Конвертировать данные в формат json
        3. Ассерт, что данные из json соответствуют ожидаемым"""

        response = r.post(self.base.API_CONSTANTS.POST.post_create(), data=self.data)
        if response.status_code == self.base.API_CONSTANTS.STATUS201:
            json = response.json()
            name_response = json.get("name")
            job_response = json.get("job")
            assert self.response.get("name") == name_response and self.response.get("job") == job_response
            print("Тест пройден!")
        else:
            print("Ошибка:" + str(response.status_code))


create = Create()
create.test_create()
