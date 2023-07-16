import requests as r
from rootpackage.api_constants import ApiConstants
from selenium import webdriver


class Base:

    def __init__(self):
        self.API_CONSTANTS = self.__API_CONSTANTS
        self.requests = requests()

    # Объекты
    __API_CONSTANTS = ApiConstants()

    # Методы

    @staticmethod
    def assert_equals(x, y):
        """Метод на ассерт значений"""
        assert x == y
