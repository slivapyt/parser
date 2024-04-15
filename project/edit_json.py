import json

class EditJson():
  


  @staticmethod
  def json_dump(params):
      try:
          with open("parser/project/library.json", 'r' ,encoding="utf-8") as file:
              existing_data = json.load(file)
      except (FileNotFoundError, json.decoder.JSONDecodeError):
          existing_data = []
      
      if isinstance(params, dict):
          existing_data.append(params)
      
      with open("parser/project/library.json", 'w',encoding="utf-8") as file:
          json.dump(existing_data, file, ensure_ascii=False, indent=4)




  @staticmethod
  def favorites_read():  
   try:
        with open("parser/project/library.json") as file:
            favorites = json.load(file)
            return favorites
   except:
        return []


  @staticmethod
  def del_all_params():
    with open("parser/project/library.json", "w", encoding="utf-8") as file:
        file.truncate(0)

  @staticmethod
  def del_vacancy(ind):
    with open("parser/project/library.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if ind < len(data):
          del data[ind]
          with open("parser/project/library.json","w", encoding="utf-8") as file:
             json.dump(data, file, ensure_ascii=False, indent=4)
    with open("parser/project/library.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

