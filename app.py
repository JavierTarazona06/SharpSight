import json
from data import Results,ResultsAVL
import menu

def __init__():
    #menu.startMenu()
    resulAVL_imp = ResultsAVL.results_AVL_imp()
    print(resulAVL_imp.orderListPriceReverse())

__init__()
