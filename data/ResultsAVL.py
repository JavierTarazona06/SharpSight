

import pandas as pd

from data.AVL import AVL
from data.NodeT import NodeT
from data.Product import Product


class ResultsAVL():

    def __init__(self, filePath):
        self.lector = pd.read_csv(f'{filePath}')
        # Creacion
        self.tree_data = AVL()
        self.insertProducts()

    # Insercion Nodo
    def insertProducts(self):
        for i in range(self.lector.shape[0]):
            curProduct = Product(title=self.lector['titulo'][i], price=self.lector['precio'][i],
                                 link=self.lector['link'][i], brand=self.lector['marca'][i])
            self.tree_data.insertRep(curProduct)

    def __str__(self):
        return str(self.tree_data.preOrder())
    
    # Actualizacion
    def orderListPrice(self) -> str:
        return self.tree_data.inOrder()

    def orderListPriceReverse(self) -> str:
        return self.tree_data.inOrderInv()

    def bestProduct(self) -> list:
        cur_prod_node : NodeT = self.tree_data.min()
        min_prod : Product = self.tree_data.min().key
        best_prod_list : list = []
        best_prod_list.append(min_prod)
        flag : bool = True
        while (self.tree_data.next(cur_prod_node) is not None) and flag:
            if (self.tree_data.next(cur_prod_node).key == min_prod):
                best_prod_list.append(self.tree_data.next(cur_prod_node).key)
                cur_prod_node = self.tree_data.next(cur_prod_node)
            else:
                flag = False
        return best_prod_list

    def filterGreater(self,price):
        self.list_data.filterPriceGreater(price)

    def filterLower(self,price):
        self.list_data.filterPriceLower(price)

def results_AVL_imp():
    myImplementation = ResultsAVL("src/productos.csv")
    return myImplementation