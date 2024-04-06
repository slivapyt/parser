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
