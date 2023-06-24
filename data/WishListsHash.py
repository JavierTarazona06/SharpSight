
import json
import os

from data.HashTable import HashTable


class WishListsHash:

    def __init__(self) -> None:
        self.data_path = "src/WishLists.json"

        if not os.path.exists(self.data_path):
            data_file = open(self.data_path, "w", encoding="utf-8")
            data_file.close()

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}

        #From data key is wish list id and value a dict. of the 'name' and 'content' of the wish list

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

        print(data)

        if len(data.keys())==0:
            id = 0
        else:
            id = max([int(id) for id in data.keys()]) + 1

        return id
    
    def find(self, wish_list_id) -> bool:
        return self.data_hash_table.find(wish_list_id)

    def create(self, wish_list_name, wish_list_content:json) -> int:

        get_new_id_wish_list = self.get_new_id()
        wish_list_value = {"name":wish_list_name, "content":wish_list_content}

        self.data_hash_table.insert(get_new_id_wish_list, wish_list_value)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def set(self, wish_list_id:int, name:str=None, wish_list_content:json=None):
        find_wish_list = self.data_hash_table.find(wish_list_id)

        if not find_wish_list:
            raise Exception(f"Wish list con ID {wish_list_id} no existe")
        else:
            wish_list_value:dict = self.data_hash_table.get(wish_list_id)
            if name and wish_list_id:
                wish_list_value["name"] = name
                wish_list_value["content"] = wish_list_content
            elif not name:
                wish_list_value["content"] = wish_list_content
            elif not wish_list_content:
                wish_list_value["name"] = name
            self.data_hash_table.set(wish_list_id, wish_list_value)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def delete_wish_list(self, wish_list_id:int):
        find_wish_list = self.data_hash_table.find(wish_list_id)

        if not find_wish_list:
            raise Exception(f"Wish list con ID {wish_list_id} no existe")
        else:
            self.data_hash_table.remove(wish_list_id)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()