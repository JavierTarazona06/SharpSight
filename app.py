import json
import os
from data.GraphProductsBySeller import GraphProductsBySeller
from data.Graph import Graph
from data.Node import Node
from data.LinkedList import LinkedList
from data.HashTable import HashTable
from data.Product import Product
from Scrapping import Search
from data import Results,ResultsAVL
import menu
from data.WishListHeap import WishListHeap
from data.ComparisonListAVL import ComparisonListAVL
from data.SetSeller import SetSeller
from data.UserWhListHash import UserWListHash

#Data Base
from config.Data_base import data_base
from Models.user import User

def __init__():
    u_wl_h = UserWListHash()
    u_wl_h.insert(1,1)
    u_wl_h.insert(2,0)

    
    '''
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

    print(id)

    users_hash_table = HashTable()
    users_hash_table.from_dict_to_hashTable(users_data)

    flag_to_insert = True

    for user_hash in users_hash_table:
        if "n1om" == user_hash.value.get("email"):
            flag_to_insert = False
            break

    if flag_to_insert:

        cur_user = {"nombre":str("nom"), "apellido":str("nom"), "email":str("n1om"), "password":str("nom")}

        users_hash_table.insert(id, cur_user)

        users_data = users_hash_table.to_dict()

        users_file = open(users_path, "w", encoding="utf-8")
        json.dump(users_data, users_file, ensure_ascii=False, indent=4)
        users_file.close()

        print(users_data)

    else:
        raise Exception(f"El usuario con email {id} ya existe")
    '''
        
    '''
    archivo = open("src/Users.json", "w", encoding="utf-8")
    json.dump({"a":"es"}, archivo, ensure_ascii=False, indent=4)
    archivo.close()
    '''

    #menu.startMenu()
    #Search.Search(str("Nintendo Switch"))
    ###resulAVL_imp = ResultsAVL.results_AVL_imp()
    #print("-------------------------")
    #print(resulAVL_imp.view_results())


    #whishListHeap_imp = WishListHeap()
    #whishListHeap_imp.insert(resulAVL_imp.tree_data.root.key)
    #wishListHeap_imp.insert(resulAVL_imp.tree_data.root.right.key)
    #print(whishListHeap_imp.view_whish_list_json())

    #comparison = ComparisonListAVL()
    #prod = Product(title="string", price=0, link="string", seller="string",image="string",brand="string")
    #comparison.delete(resulAVL_imp.tree_data.root.key)
    #print(comparison.compareByPrice_json())



    #db = data_base()
    #db.close()

    #juan = User(email="Juan2@juan.com", password="pato_feliz", operation=1)
    #juan = User(email="Juan@juan.com", password="pato_feliz", operation=2, name="Juan", last_name="Perez")
    #juan = User(email="Juan2@juan.com", password="pato_feliz", operation=2, name="Juan2", last_name="Perez2")
    #juan.update(name="Juana", last_name="Perez", email="pepa@pepa.com", password="pata_feliz")
    #print(juan.json())

    #mySet = SetSeller()
    #print(mySet.products)
    #print("------------------------------")
    #print(mySet.setSellers)
    #print("------------------------------")
    #print(mySet.sellers_json())
    #print("------------------------------")
    #print("------------------------------")
    #print(mySet.products_seller_json('Ktronix'))
    pass



__init__()
