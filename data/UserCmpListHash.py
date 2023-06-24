
import json
import os
from data.HashTable import HashTable

class UserCmpListHash:

    def __init__(self) -> None:
        self.data_path = "src/Users_comparisonList.json"

        if not os.path.exists(self.data_path):
            data_file = open(self.data_path, "w", encoding="utf-8")
            data_file.close()

        if os.path.getsize(self.data_path) > 0:
            data_file = open(self.data_path, "r", encoding="utf-8")
            data: dict = json.load(data_file)
            data_file.close()
        else:
            data = {}

        #From data key is user id and value the list of comparison lists ID's

        self.data_hash_table = HashTable()
        self.data_hash_table.from_dict_to_hashTable(data)

        print(self.data_hash_table)

    def comparison_lists_by_user(self, user_id) -> list:
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            raise Exception(f"El usuario con id {user_id} no tiene comparison lists")
        else:
            cur_comparison_list_ids:list = self.data_hash_table.get(user_id)
            return cur_comparison_list_ids


    def insert(self, user_id:int, comparison_list_id:int):
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            self.data_hash_table.insert(user_id, [comparison_list_id])
        else:
            cur_comparison_list_ids:list = self.data_hash_table.get(user_id)
            print(cur_comparison_list_ids)
            if comparison_list_id in cur_comparison_list_ids:
                raise Exception(f"comparison list {comparison_list_id} already added for user {user_id}")
            else:
                cur_comparison_list_ids.append(comparison_list_id)
                self.data_hash_table.set(user_id, cur_comparison_list_ids)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def delete_comparison_list(self, user_id:int, comparison_list_id:int):
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            raise Exception(f"Usuario {user_id} no tiene comparison lists guardadas")
        else:
            cur_comparison_list_ids:list = self.data_hash_table.get(user_id)
            if comparison_list_id in cur_comparison_list_ids:
                cur_comparison_list_ids.remove(comparison_list_id)
                if len(cur_comparison_list_ids) == 0:
                    self.data_hash_table.remove(user_id)
                else:
                    self.data_hash_table.set(user_id, cur_comparison_list_ids)
            else:
                raise Exception(f"Usuario {user_id} no tiene guardada la lista de desos {comparison_list_id}")

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()

    def delete_all(self, user_id:int):
        find_user = self.data_hash_table.find(user_id)

        if not find_user:
            raise Exception(f"Usuario {user_id} no tiene comparison lists guardadas")
        else:
            self.data_hash_table.remove(user_id)

        data = self.data_hash_table.to_dict()
        data_file = open(self.data_path, "w", encoding="utf-8")
        json.dump(data, data_file, ensure_ascii=False, indent=4)
        data_file.close()