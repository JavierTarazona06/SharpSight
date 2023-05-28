import json
from data.Product import Product
from Scrapping import Search
from data import Results,ResultsAVL
import menu
from data.WishListHeap import WishListHeap
from data.ComparisonListAVL import ComparisonListAVL

def __init__():
    #menu.startMenu()
    #Search.Search("Lavadora")
    resulAVL_imp = ResultsAVL.results_AVL_imp()
    #print(resulAVL_imp.orderListPrice())


    #whishListHeap_imp = WishListHeap()
    #whishListHeap_imp.insert(resulAVL_imp.tree_data.root.key)
    #wishListHeap_imp.insert(resulAVL_imp.tree_data.root.right.key)
    #print(whishListHeap_imp.view_whish_list_json())

    
    comparison = ComparisonListAVL()
    prod = Product(title="string", price=0, link="string", seller="string",image="string",brand="string")
    #comparison.delete(resulAVL_imp.tree_data.root.key)
    comparison.delete(prod)
    print(comparison)
    print(comparison.view_comparison_list_json())

    #whishList.delete_min()

    


__init__()
