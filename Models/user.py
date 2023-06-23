#Data Base
import csv
import json
import os

import pandas as pd
from pathlib import Path
from data.HashTable import HashTable
from config.Data_base import data_base
from passlib.hash import bcrypt

class User:

    def __init__(self, email:str, password:str, operation:int, name:str=None, last_name:str=None) -> None:
        self.id = None
        self.name = None
        self.last_name = None
        self.email = str(email)
        self.password = str(password)
        if operation==1:
            #self.get_from_DB()
            self.get()
        elif operation==2:
            if (name is None) or (last_name is None):
                raise Exception("No se puede crear usuario ya que el nombre y/o el apellido son nulos")
            else:
                #self.post_to_DB(name, last_name)
                self.post(name, last_name)
        else:
            raise Exception(f"No existe operación número {operation}")


    def __str__(self) -> str:
        return f"{self.id}: {self.name} {self.last_name} {self.email}"
    
    def json(self) -> list:
        result = {}
        result["id"] = int(self.id)
        result["nombre"] = str(self.name)
        result["apellido"] = str(self.last_name)
        result["email"] = str(self.email)
        result["password"] = str(self.password)
        return result
    
    def post(self, name, last_name):
        if (not '@' in self.email) or (not '.com' in self.email):
            raise Exception("La dirección de correo no es válida")


        hashed_password = bcrypt.hash(self.password)

        users_path = "src/Users.json"

        if not os.path.exists(users_path):
            users_file = open(users_path, "w", encoding="utf-8")
            users_file.close()

        print(os.path.getsize(users_path))
        if os.path.getsize(users_path) > 0:
            users_file = open(users_path, "r", encoding="utf-8")
            users_data: dict = json.load(users_file)
            users_file.close()
        else:
            users_data = {}

        print(users_data)

        if len(users_data.keys())==0:
            id = 0
        else:
            id = max([int(id) for id in users_data.keys()]) + 1

        self.id = id
        self.name = name
        self.last_name = last_name
        self.password = hashed_password

        users_hash_table = HashTable()
        users_hash_table.from_dict_to_hashTable(users_data)

        flag_to_insert = True

        for user_hash in users_hash_table:
            if self.email == user_hash.value.get("email"):
                flag_to_insert = False
                break

        if flag_to_insert:

            cur_user = {"nombre":str(self.name), "apellido":str(self.last_name), "email":str(self.email), "password":str(self.password)}

            users_hash_table.insert(int(id), cur_user)

            users_data = users_hash_table.to_dict()

            users_file = open(users_path, "w", encoding="utf-8")
            json.dump(users_data, users_file, ensure_ascii=False, indent=4)
            users_file.close()

            print(f"Usuario {self.email} creado exitosamente")

        else:
            raise Exception(f"El usuario con email {self.email} ya existe")




    def post_to_DB(self, name, last_name):

        hashed_password = bcrypt.hash(self.password)
        self.password = hashed_password

        db = data_base()
        query = f"insert into users (name_user, last_name_user, email_user, password_user) values ('{name}','{last_name}','{self.email}','{self.password}');"
        db.cursor.execute(query)

        query = f"select id_user from users where email_user='{self.email}';"
        db.cursor.execute(query)
        result_id = db.cursor.fetchone()[0]

        db.connection.commit()

        db.close()
        
        self.id = int(result_id)
        self.name = str(name)
        self.last_name = str(last_name)

        print(f"Usuario {self.email} creado en DB exitosamente")

    def get(self):

        users_path = "src/Users.json"

        try:
            users_file = open(users_path, "r", encoding="utf-8")
            users_data: dict = json.load(users_file)
            users_file.close()
        except Exception as e:
            raise Exception(f"No hay usuarios guardados. Error: {e}")
        
        users_hash_table = HashTable()
        users_hash_table.from_dict_to_hashTable(users_data)

        find = False

        for user_hash in users_hash_table:
            if self.email == user_hash.value.get("email"):
                self.id = int(user_hash.key)
                self.name = user_hash.value.get("nombre")
                self.last_name = user_hash.value.get("apellido")
                hashed_password = user_hash.value.get("password")
                find = True
                break

        if not find:
            raise Exception(f"Usuario no encontrado con email {self.email}")
        
        is_valid = bcrypt.verify(self.password,hashed_password)
        if is_valid:
            self.password = hashed_password
            print("Clave válida")
        else:
            raise Exception(f"Clave inválida para usuario {self.email}")


    def get_from_DB(self):
        
        db = data_base()

        query_hashedPassword = f"select password_user from users where email_user='{self.email}';"
        db.cursor.execute(query_hashedPassword)
        result_hashedPassword = db.cursor.fetchone()

        if result_hashedPassword:
            hashed_password = result_hashedPassword[0]
            is_valid = bcrypt.verify(self.password,hashed_password)
            if is_valid:
                self.password = hashed_password
                print("Clave válida")
            else:
                raise Exception(f"Clave inválida para usuario {self.email}")
        else:
            raise Exception(f"No existe clave para usuario o usuario {self.email}")
        
        query = f"select id_user,name_user,last_name_user from users where email_user='{self.email}';"
        db.cursor.execute(query)
        result = db.cursor.fetchone()

        self.id = int(result[0])
        self.name = str(result[1])
        self.last_name = str(result[2])

        db.connection.commit()

        db.close()

    def update(self, name:str=None, last_name:str=None, email:str=None, password:str=None):
        if (not '@' in self.email) or (not '.com' in self.email and not '.co' in self.email):
            raise Exception("La dirección de correo no es válida")

        if name == "":
            name = None
        if last_name == "":
            last_name = None
        if email == "":
            email = None
        if password == "":
            password = None
        
        users_path = "src/Users.json"

        try:
            users_file = open(users_path, "r", encoding="utf-8")
            users_data: dict = json.load(users_file)
            users_file.close()
        except Exception as e:
            raise Exception(f"No hay usuarios guardados. Error: {e}")
        
        users_hash_table = HashTable()
        users_hash_table.from_dict_to_hashTable(users_data)

        flag_email = True
        for user_hash in users_hash_table:
            if email == user_hash.value.get("email"):
                flag_email = False
                break
        if not flag_email:
            raise Exception(f"El usuario con email {email} ya existe")

        if name is not None:
            users_hash_table.get(self.id)["nombre"] = str(name)
            self.name = name
        if last_name is not None:
            users_hash_table.get(self.id)["apellido"] = str(last_name)
            self.last_name = last_name
        if email is not None:
            users_hash_table.get(self.id)["email"] = str(email)
            self.email = email
        if password is not None:
            hashed_password = bcrypt.hash(password)
            users_hash_table.get(self.id)["password"] = str(hashed_password)
            self.password = hashed_password

        users_data = users_hash_table.to_dict()

        users_file = open(users_path, "w", encoding="utf-8")
        json.dump(users_data, users_file, ensure_ascii=False, indent=4)
        users_file.close()


    def update_db(self, name:str=None, last_name:str=None, email:str=None, password:str=None):

        db = data_base()

        if name is not None:
            query = f"update users set name_user='{name}' where id_user={self.id}"
            db.cursor.execute(query)
            self.name = name
        if last_name is not None:
            query = f"update users set last_name_user='{last_name}' where id_user={self.id}"
            db.cursor.execute(query)
            self.last_name = last_name
        if email is not None:
            query = f"update users set email_user='{email}' where id_user={self.id}"
            db.cursor.execute(query)
            self.email = email
        if password is not None:
            hashed_password = bcrypt.hash(password)
            query = f"update users set password_user='{hashed_password}' where id_user={self.id}"
            db.cursor.execute(query)
            self.password = hashed_password

        db.connection.commit()

        db.close()

    def delete(self):
        users_path = "src/Users.json"

        try:
            users_file = open(users_path, "r", encoding="utf-8")
            users_data: dict = json.load(users_file)
            users_file.close()
        except Exception as e:
            raise Exception(f"No hay usuarios guardados. Error: {e}")
        
        users_hash_table = HashTable()
        users_hash_table.from_dict_to_hashTable(users_data)

        users_hash_table.remove(self.id)
        
        users_data = users_hash_table.to_dict()
        users_file = open(users_path, "w", encoding="utf-8")
        json.dump(users_data, users_file, ensure_ascii=False, indent=4)
        users_file.close()

    def delete_db(self):
        
        db = data_base()
        query = f"delete from users where id_user={self.id};"
        db.cursor.execute(query)
        db.connection.commit()
        print(f"Se eliminó el usuario {self.name} exitosamente")
        db.close()