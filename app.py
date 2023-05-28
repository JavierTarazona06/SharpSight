import json
from Scrapping import Search
from data import Results,ResultsAVL
import menu
from data.WishListHeap import WishListHeap

def __init__():
    #menu.startMenu()
    #print(resulAVL_imp.orderListPrice())
    #Search.Search("Nintendo Switch")
    resulAVL_imp = ResultsAVL.results_AVL_imp()
    whishList = WishListHeap()
    #whishList.insert(resulAVL_imp.tree_data.root.right.key)
    whishList.delete(resulAVL_imp.tree_data.root.right.key)

    #whishList.delete_min()

    


__init__()
