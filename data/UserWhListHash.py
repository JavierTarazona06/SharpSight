
import json
import os
from data.HashTable import HashTable


class UserWListHash:

    def __init__(self) -> None:
        self.data_path = "src/Users_WishList.json"

        if not os.path.exists(self.data_path):
            data_file = open(self.data_path, "w", encoding="utf-8")
            data_file.close()

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}

        #From data key is user id and value the list of wish lists ID's

        self.data_hash_table = HashTable()
        self.data_hash_table.from_dict_to_hashTable(data)

        print(self.data_hash_table)

    def insert(self, user_id:int, wish_list_id:int):
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            self.data_hash_table.insert(user_id, [wish_list_id])
        else:
            cur_wish_list_ids:list = self.data_hash_table.get(user_id)
            print(cur_wish_list_ids)
            if wish_list_id in cur_wish_list_ids:
                raise Exception(f"Wish list {wish_list_id} already added for user {user_id}")
            else:
                cur_wish_list_ids.append(wish_list_id)
                self.data_hash_table.set(user_id, cur_wish_list_ids)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def delete_wish_list(self, user_id:int, wish_list_id:int):
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            raise Exception(f"Usuario {user_id} no tiene listas de deseos guardadas")
        else:
            cur_wish_list_ids:list = self.data_hash_table.get(user_id)
            if wish_list_id in cur_wish_list_ids:
                cur_wish_list_ids.remove(wish_list_id)
                if len(cur_wish_list_ids) == 0:
                    self.data_hash_table.remove(user_id)
                else:
                    self.data_hash_table.set(user_id, cur_wish_list_ids)
            else:
                raise Exception(f"Usuario {user_id} no tiene guardada la lista de desos {wish_list_id}")

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def delete_all(self, user_id:int):
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            raise Exception(f"Usuario {user_id} no tiene listas de deseos guardadas")
        else:
            self.data_hash_table.remove(user_id)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()