import requests
import json
from bs4 import BeautifulSoup as BS
from abstract import JobPlatform


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
            try:
                profession = vacancy["profession"]
            except KeyError:
                profession = "нет данных"

            try:
                payment_to = vacancy["payment_to"]
                if payment_to == None:
                    payment_to =""

            except TypeError:
                payment_to = ""
                
            try:
                payment_from = vacancy["payment_from"]
                if payment_from == None:
                    payment_from =""                
            except TypeError:
                payment_from = ""
            
            payment = self.format_payment(payment_to, payment_from)

            try:
                address = vacancy["address"]
            except KeyError:
                address = "нет данных"

            try:
                link = vacancy["client"]["link"]
            except KeyError:
                link = "нет данных"  

            try:
                town = vacancy["town"]["title"]
            except KeyError:
                town = "нет данных"  

            vacancy_list.append(
                {
                    "profession": profession,
                    "payment": payment,
                    "address": address, 
                    "link": link, 
                    "town": town
                    })
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



teta1 = Superjob("слесарь")
ss = teta1.create_params_vacancy()
for i in ss:
    print(i)

class HeadHunter(JobPlatform):

    def __init__(self, keyword):
        self.__header = {
            "User-Agent": "Brave/1.64 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"
            }
        self.__params = {
        "text": keyword,
        "page": 0,
        "per_page": 100,
        }
        self.__vacancies = []


    def get_request(self):
        response = requests.get("https://api.hh.ru/vacancies",
                                headers=self.__header,
                                params=self.__params)
        js_response = response.json()["items"]
        return js_response
    

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




    def format_payment(self, payment_to, payment_from):
        if not payment_to and not payment_from:
            payment = "зп не указанна"
            
        elif not payment_from:
            payment = payment_to
            
        elif not payment_to:
            payment = payment_from
        else:
            payment = f'{payment_from} - {payment_to}'
        return payment
        

    def create_params_vacancy(self):
        vacancy_list = []
        vacancies = self.get_value_vacancies()

        for vacancy in vacancies:
            try:
                profession = vacancy["name"]
            except KeyError:
                profession = "нет данных"

            try:
                payment_to = vacancy["salary"]["to"]
                if payment_to == None:
                    payment_to =""

            except TypeError:
                payment_to = ""
                
            try:
                payment_from = vacancy["salary"]["from"]
                if payment_from == None:
                    payment_from =""                
            except TypeError:
                payment_from = ""
            
            payment = self.format_payment(payment_to, payment_from)

            try:
                address = vacancy["street"]
            except KeyError:
                address = "нет данных"

            try:
                link = vacancy["alternate_url"]
            except KeyError:
                link = "нет данных"  

            try:
                town = vacancy["city"]
            except KeyError:
                town = "нет данных"  


            vacancy_list.append(
                {
                    "profession": profession,
                    "payment": payment,
                    "link": link,
                    "address": address,
                    "town": town
                })

        return vacancy_list




# "address": vacancy["street"],
# ,"town": vacancy["city"]







# teta = HeadHunter("craft")
# ss = teta.create_params_vacancy()

# for i in ss:
#     print(i)
# print(teta.create_params_vacancy())







# keyword = None
# header = {"User-Agent": "Brave/1.64 (platform; rv:get_version) Gecko/geckotrail Firefox/firefoxversion"
# }
# params = {
#     "text": keyword,
#     "page": 0,
#     "per_page": 1,
# }

# response = requests.get("https://api.hh.ru/vacancies",
#                                 headers=header, params=params)
# js_response = response.json()
#js_response = json.dumps(js_response, indent=4)
# print(js_response)
# print(js_response["items"][0]["street"])