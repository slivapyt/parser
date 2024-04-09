from abc import ABC, abstractmethod


class JobPlatform(ABC):

    @abstractmethod
    def get_request(self):
        pass

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


    def get_value_vacancies(self, pages_count=1, params,):
        while self.__params["page"] < pages_count:
            try:
                values = self.get_request()
            except Exception:
                print("ошибка при парсинге")
                break
            self.__vacancies.extend(values)
            self.__params["page"] += 1
        return self.__vacancies