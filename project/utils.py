import requests
import json
from bs4 import BeautifulSoup as BS
from project.abstract import JobPlatform


class Superjob(JobPlatform):
    def __init__(self, keyword):
        self.__header = {
            "X-Api-App-Id": "v3.r.134200068.75e341f5916df9666f8909259e60ce83b2026edf.64c4b514605c301726c41bd3a0c400385f8c4e9f"}
        self.__params = {
            "keyword": keyword,
            "page": 0,
            "count": 100,
        }
        self.__vacancies = []

    def get_request(self):
        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                headers=self.__header, params=self.__params)
        js_response = response.json()["objects"]
        return js_response



    def create_params_vacancy(self):
        vacancy_list = []
        vacancies = self.get_value_vacancies()
        for vacancy in vacancies:
            vacancy_list.append(
                {"profession": vacancy["profession"], "payment": f'{vacancy["payment_from"]} - {vacancy["payment_to"]}',
                    "address": vacancy["address"], "link": vacancy["client"]["link"], "town": vacancy["town"]["title"]})
        return vacancy_list

    def get_value_vacancies(self, pages_count=1):
        while self.__params["page"] < pages_count:
            try:
                values = self.get_request()
            except Exception:
                print("ошибка при парсинге")
                break
            self.__vacancies.extend(values)
            self.__params["page"] += 1
        return self.__vacancies


superjob = Superjob("craft") # тэг реализовать через инпут
superjob.get_value_vacancies()
print(test.create_params_vacancy())



class HeadHunter(JobPlatform):
