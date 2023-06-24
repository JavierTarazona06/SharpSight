
import json
import os

from data.HashTable import HashTable

class ComparisonListHash:

    def __init__(self) -> None:
        self.data_path = "src/ComparisonLists.json"

        if not os.path.exists(self.data_path):
            data_file = open(self.data_path, "w", encoding="utf-8")
            data_file.close()

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}

        #From data key is comparison list id and value a dict. of the 'name' and 'content' of the comparison list

        self.data_hash_table = HashTable()
        self.data_hash_table.from_dict_to_hashTable(data)

        print(self.data_hash_table)

    def get_new_id(self) -> int:
        if not os.path.exists(self.data_path):
            data_file = open(self.data_path, "w", encoding="utf-8")
            data_file.close()

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}


        if len(data.keys())==0:
            id = 0
        else:
            id = max([int(id) for id in data.keys()]) + 1

        return id
    
    def find(self, comparison_list_id) -> bool:
        return self.data_hash_table.find(comparison_list_id)
    
    def find_id(self, name:str) -> list:
        if not os.path.exists(self.data_path):
            raise Exception("No hay Comparison Lists cargadas")

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}


        if len(data.keys())==0:
            raise Exception("No hay Comparison Lists cargadas")
        else:
            possible_ids = []
            for id in data.keys():
                if name == data[id]["name"]:
                    possible_ids.append(int(id))
                    
            return possible_ids

        raise Exception(f"No existe Comparison List con el nombre {name}")
    

    def find_name(self, id) -> str:
        id = str(id)
        if not os.path.exists(self.data_path):
            raise Exception("No hay Comparison List cargadas")

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}


        if len(data.keys())==0:
            raise Exception("No hay Comparison List cargados")
        else:
            if str(id) in data.keys():
                name = data[str(id)]["name"]
                return name
            else:
                raise Exception(f"No existen Comparison List con el id {id}")
            

    def update_name(self, id, new_name:str) -> str:
        id = str(id)
        if not os.path.exists(self.data_path):
            raise Exception("No hay Comparison List cargadas")

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}

        print(data)

        if len(data.keys())==0:
            raise Exception("No hay Comparison List cargadas")
        else:
            if str(id) in data.keys():
                data[str(id)]["name"] = new_name
                data_file = open(self.data_path, "w", encoding="utf-8")
                json.dump(data, data_file, ensure_ascii=False, indent=4)
                data_file.close()
            else:
                raise Exception(f"No existen Comparison List con el id {id}")
    

    def create(self, comparison_list_name, comparison_list_content:list) -> int:

        get_id_comparison_list = self.get_new_id()
        comparison_list_value = {"name":comparison_list_name, "content":comparison_list_content}

        self.data_hash_table.insert(get_id_comparison_list, comparison_list_value)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

        return get_id_comparison_list

    def set(self, comparison_list_id:int, name:str=None, comparison_list_content:list=None):
        find_comparison_list = self.data_hash_table.find(comparison_list_id)

        if not find_comparison_list:
            raise Exception(f"comparison list con ID {comparison_list_id} no existe")
        else:
            comparison_list_value:dict = self.data_hash_table.get(comparison_list_id)
            if name and comparison_list_id:
                comparison_list_value["name"] = name
                comparison_list_value["content"] = comparison_list_content
            elif not name:
                comparison_list_value["content"] = comparison_list_content
            elif not comparison_list_content:
                comparison_list_value["name"] = name
            self.data_hash_table.set(comparison_list_id, comparison_list_value)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def delete_comparison_list(self, comparison_list_id:int):
        find_comparison_list = self.data_hash_table.find(comparison_list_id)

        if not find_comparison_list:
            raise Exception(f"comparison list con ID {comparison_list_id} no existe")
        else:
            self.data_hash_table.remove(comparison_list_id)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()