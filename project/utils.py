from abstract import JobPlatform
import re
class Superjob(JobPlatform):

    def __init__(self, keyword):
        self.__header = {
            "X-Api-App-Id": "v3.r.134200068.75e341f5916df9666f8909259e60ce83b2026edf.64c4b514605c301726c41bd3a0c400385f8c4e9f"}
        
        self.__params = {
            "keyword": keyword,
            "page": 0,
            "count": 100}
        self.__vacancies = []
        self.values = self.get_request(
            "https://api.superjob.ru/2.0/vacancies/",
            self.__header,
            self.__params,
            "objects")


    def create_params_vacancy(self):
        vacancy_list = []
        vacancies = self.get_value_vacancies(self.__params, self.values, self.__vacancies)

        for vacancy in vacancies:

            """------------------Название вакансии----------------------------"""
            try:
                profession = vacancy["profession"]
            except KeyError:
                profession = "нет данных"


            """---------------------Зарплата----------------------------------"""
            try:
                currency = vacancy["currency"]
            except TypeError:
                currency = ""


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

            if payment == "зп не указанна":
                payment_ful = "зп не указанна"
            else:
                payment_ful = f'{payment} {currency}'
            


            """-----------------------Адрес-----------------------------------"""
            try:
                address = vacancy["address"]
            except KeyError:
                address = "нет данных"


            try:
                link = vacancy["link"]
            except KeyError:
                link = "нет данных"  


            try:
                town = vacancy["town"]["title"]
            except KeyError:
                town = "нет данных"  

            """-------------Условия и требования------------------------------"""


            """Обязанности"""
            try:
                responsibility = vacancy["work"]
            except KeyError:
                responsibility = "нет данных"  


            """Требования"""
            try:
                requirement = vacancy["candidat"]
            except KeyError:
                requirement = "нет данных"  


            """Режим работы"""
            try:
                schedule = vacancy["type_of_work"]["title"]
            except KeyError:
                schedule = "нет данных"  
            """---------------------------------------------------------------"""

            vacancy_list.append(
                {
                    "profession": profession,
                    "payment": payment_ful,
                    "address": address, 
                    "link": link, 
                    "town": town,
                    "responsibility": responsibility,
                    "requirement": requirement,
                    "schedule": schedule
                    })
            
        return vacancy_list


    def __repr__(self):
        info = self.create_params_vacancy()
        section = info[0]
        return (f'''-----------------------------------------------------\n
Вакансия: {section["profession"]}\n
-----------------------------------------------------\n
Оплата: {section["payment"]}\n
-----------------------------------------------------\n
Ссылка на вакансию: {section["link"]}\n
-----------------------------------------------------\n
Адрес: {section["address"]}\n
-----------------------------------------------------\n
Город: {section["town"]}\n
-----------------------------------------------------\n
Расписание: {section["schedule"]}\n
-----------------------------------------------------\n
Требования: {section["requirement"]}\n
-----------------------------------------------------\n
Обязанности: {section["responsibility"]}\n
''')


    def __str__(self):
        out = self.values
 
        return f"{out[0]}"



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
        self.values = self.get_request(
            "https://api.hh.ru/vacancies",
            self.__header,
            self.__params,
            "items"
            )
        

    def create_params_vacancy(self):
        vacancy_list = []
        vacancies = self.get_value_vacancies(self.__params, self.values, self.__vacancies)

        for vacancy in vacancies:
            """------------------Название вакансии----------------------------"""
            try:
                profession = vacancy["name"]
            except KeyError:
                profession = "нет данных"

            """---------------------Зарплата----------------------------------"""
            try:
                currency = vacancy["salary"]["currency"]
            except TypeError:
                currency = ""

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

            if payment == "зп не указанна":
                payment_ful = "зп не указанна"
            else:
                payment_ful = f'{payment} {currency}'
            
            """-----------------------Адрес-----------------------------------"""
            """Адрес: улица"""
            try:
                address = vacancy["address"]["street"]
            except TypeError:
                address = "нет данных"

            """Адрес: город"""
            try:
                town = vacancy["address"]["city"]
            except TypeError:
                town = "нет данных"  

            """Адрес: дом"""
            try:
                building = vacancy["address"]["building"]
            except TypeError:
                building = ""
            address_build = f'{address} {building}'

            """Адрес: ссылка"""
            try:
                link = vacancy["alternate_url"]
            except KeyError:
                link = "нет данных"  


            """-------------Условия и требования------------------------------"""
            """Режим работы"""
            try:
                schedule = vacancy["schedule"]["name"]
            except TypeError:
                schedule = "нет данных"  


            """Требования"""
            try:
                requirement = vacancy["snippet"]["requirement"]
                if "<highlighttext>" in requirement:
                    requirement = requirement.replace("<highlighttext>","</highlighttext>","")
            except TypeError:
                requirement = "нет данных"  

            """Обязанности"""
            try:
                responsibility = vacancy["snippet"]["responsibility"]
                if "<highlighttext>" in responsibility:
                    responsibility = responsibility.replace("<highlighttext>","</highlighttext>","")
            except TypeError:
                responsibility = "нет данных"  
            """---------------------------------------------------------------"""

            vacancy_list.append(
                {
                    "profession": profession,
                    "payment": payment_ful,
                    "link": link,
                    "address": address_build,
                    "town": town,
                    "schedule": schedule,
                    "requirement": requirement,
                    "responsibility":responsibility


                })

        return vacancy_list



    def __repr__(self):
        info = self.create_params_vacancy()
        section = info[0]
        return (f'''-----------------------------------------------------\n
Вакансия - {section["profession"]}\n
-----------------------------------------------------\n
Оплата - {section["payment"]}\n
-----------------------------------------------------\n
Ссылка на вакансию - {section["link"]}\n
-----------------------------------------------------\n
Адрес - {section["address"]}\n
-----------------------------------------------------\n
Город - {section["town"]}\n
-----------------------------------------------------\n
Расписание - {section["schedule"]}\n
-----------------------------------------------------\n
Требования - {section["requirement"]}\n
-----------------------------------------------------\n
Обязанности - {section["responsibility"]}\n
''')
 

    def __str__(self):
        out = self.create_params_vacancy()
 
        return f"{out}"



class Main():

  @staticmethod
  def processing_request(platform, vacancy):
    if platform == "1":
      super_jpb = Superjob(vacancy)
      super_jpb_vacancy = super_jpb.create_params_vacancy()
      return super_jpb_vacancy

    elif platform == "2":
      head_hunter = HeadHunter(vacancy)
      head_hunter_vacancy = head_hunter.create_params_vacancy()
      return head_hunter_vacancy

    elif platform == "3":
      super_jpb = Superjob(vacancy)
      super_jpb_vacancy = super_jpb.create_params_vacancy()

      head_hunter = HeadHunter(vacancy)
      head_hunter_vacancy = head_hunter.create_params_vacancy()
      
      all_platform_vacancy = super_jpb_vacancy + head_hunter_vacancy
      return all_platform_vacancy
    
    else:
      print("некорректный ввод")


  @staticmethod
  def output(vacancy_list):

    return (f'''-----------------------------------------------------\n
Вакансия - {vacancy_list["profession"]}\n
-----------------------------------------------------\n
Оплата - {vacancy_list["payment"]}\n
-----------------------------------------------------\n
Ссылка на вакансию - {vacancy_list["link"]}\n
-----------------------------------------------------\n
Адрес - {vacancy_list["address"]}\n
-----------------------------------------------------\n
Город - {vacancy_list["town"]}\n
-----------------------------------------------------\n
Расписание - {vacancy_list["schedule"]}\n
-----------------------------------------------------\n
Требования - {vacancy_list["requirement"]}\n
-----------------------------------------------------\n
Обязанности - {vacancy_list["responsibility"]}\n
''')
  
  
  @staticmethod
  def get_top(list_vacancy):
   new_list = sorted(list_vacancy, key= lambda x: re.findall(r'\d+', x["payment"]), reverse=True)
   top_10_payments = new_list[:10]
   return top_10_payments
  

  @staticmethod
  def navigation(count, page):
    if count == ">":
      page += 1

    elif count == "<":
      page -= 1

    elif count == "":
      page = 0
    
    else:
      try:
        page = int(count) -1 
      except:
          pass  
    return page
  
  @staticmethod
  def filter(vacancy_list, key):
      filtered_list = []
      for i in vacancy_list:
          if key in i["requirement"] or key in i["responsibility"]:
              filtered_list.append(i)
      return filtered_list
              
      
      
      

  def del_request(self):
    pass





















# request_headhunter = HeadHunter("слесарь")
# params = request_headhunter.create_params_vacancy()
# request_headhunter.json_dump(params)
# print(repr(request_headhunter))

# HeadHunter = request_headhunter.create_params_vacancy()
# for i in HeadHunter:
#     print(i)


# request_superjob = Superjob("хирург")
# params = request_superjob.create_params_vacancy()
# request_superjob.json_dump(params)
#print(repr(request_Superjob))

#print(request_superjob)
# superjob = request_superjob.create_params_vacancy()
# for i in superjob:
#     print(i)

# print(json.dumps(i, indent=4,ensure_ascii=False))