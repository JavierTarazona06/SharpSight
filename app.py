import json
from data.Product import Product
from Scrapping import Search
from data import Results,ResultsAVL
import menu
from data.WishListHeap import WishListHeap
from data.ComparisonListAVL import ComparisonListAVL
from data.SetSeller import SetSeller

#Data Base
from config.Data_base import data_base
from Models.User import User

def __init__():
    #menu.startMenu()
    #Search.Search(str("Nintendo Switch"))
    resulAVL_imp = ResultsAVL.results_AVL_imp()
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



__init__()
