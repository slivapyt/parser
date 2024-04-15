from utils import Superjob, HeadHunter, Main
from edit_json import EditJson


page = 0
count = ""
'''генерация вакансий'''
print("Какая платформа интересует")
platform = input("1 - Superjob, 2 - HeadHunter, 3 - Анкеты со всех доступных платформ\n")
vacancy = input("Укажите интересующую вас вакансию\n")
check = Main()
vacancy_list = check.processing_request(platform, vacancy)

default_list = check.processing_request(platform, vacancy)
top_list = check.get_top(vacancy_list)


edit_json = EditJson()



while True:

  if page >= 0:
    favorites = edit_json.favorites_read()
    try:
      print(check.output(vacancy_list[page]))
    except IndexError:
      page = 0
      continue
    print(f"станица № {page+1} из {len(vacancy_list)}\n (<), (>), num page, exit(X), save(S), clear favorites(clr),")
    if vacancy_list == top_list:
      print("топ")

    if vacancy_list == favorites:
      print("избранное")
      
    count = input()



    '''навигация'''
    page = check.navigation(count, page)


    #сохранить
    if count.lower() == "s":
      print("вакансия сохранена")
      edit_json.json_dump(vacancy_list[page])
    

    #отчистить избранное
    elif count.lower() == "clr":
      print("избранное очищено")
      edit_json.del_all_params()


    #удаление элемента
    elif count.lower() == "del":
      if vacancy_list == favorites:
        edit_json.del_vacancy(page)
        vacancy_list = edit_json.favorites_read()
        page = 0


    #выход
    elif count.lower() == "x":
      break
  

    #топ
    elif count.lower() == "top":
      if vacancy_list == default_list or vacancy_list == favorites:
        vacancy_list = top_list
        page = 0
      else:
        vacancy_list = default_list
        page = 0



    #избранное
    elif count.lower() == "fav":
      if vacancy_list == default_list or vacancy_list == top_list:
        vacancy_list = favorites
        page = 0
      else:
        vacancy_list = default_list
        page = 0

