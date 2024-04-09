from abc import ABC, abstractmethod
import requests

class JobPlatform(ABC):

    # @abstractmethod
    # def get_request(self):
    #     pass

    @abstractmethod
    def create_params_vacancy(self):
        pass

    @abstractmethod
    def get_value_vacancies(self):
        pass


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


    def get_value_vacancies(self, params,req_values,vacancies, pages_count = 1):
        while params["page"] < pages_count:
            try:
                values = req_values
            except Exception:
                print("ошибка при парсинге")
                break
            vacancies.extend(values)
            params["page"] += 1
        return vacancies
    

    def get_request(self, link, header, params, title_val):
        response = requests.get(link, 
                                headers = header,
                                params = params)
        js_response = response.json()[title_val]
        return js_response