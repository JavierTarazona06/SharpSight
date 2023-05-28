

import pandas as pd
from data.DynamicList import DynamicList

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
                                 link=self.lector['link'][i], seller=self.lector['marca'][i])
            self.tree_data.insert(curProduct)

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
        best_prod_list.append(str(min_prod))
        flag : bool = True
        while (self.tree_data.next(cur_prod_node) is not None) and flag:
            if (self.tree_data.next(cur_prod_node).key == min_prod):
                best_prod_list.append(str(self.tree_data.next(cur_prod_node).key))
                cur_prod_node = self.tree_data.next(cur_prod_node)
            else:
                flag = False
        return best_prod_list
    
    
    def bestProduct_json(self) -> list:
        cur_prod_node : NodeT = self.tree_data.min()
        min_prod : Product = self.tree_data.min().key
        best_prod_list : list = []
        best_prod_list.append(min_prod.json())
        flag : bool = True
        while (self.tree_data.next(cur_prod_node) is not None) and flag:
            if (self.tree_data.next(cur_prod_node).key == min_prod):
                best_prod_list.append(self.tree_data.next(cur_prod_node).key.json())
                cur_prod_node = self.tree_data.next(cur_prod_node)
            else:
                flag = False
        return best_prod_list
    
    def findCall_price(self, toSearch_price:int, ptr:NodeT) -> NodeT:
        cur_product : Product = ptr.key
        if toSearch_price == cur_product.price:
            return ptr
        elif toSearch_price > cur_product.price:
            if ptr.right is not None:
                return self.findCall_price(toSearch_price, ptr.right)
            else:
                return ptr
        else:
            if ptr.left is not None:
                return self.findCall_price(toSearch_price, ptr.left)
            else:
                return ptr

    def find_price(self, toSearchPrice:int) -> NodeT:
        found : NodeT = self.findCall_price(toSearchPrice, self.tree_data.root)
        if (found.key.price < toSearchPrice) and self.tree_data.next(found) is not None:
            found = self.tree_data.next(found)
        return found
    
    def rangeSearch(self, x:int, y:int) -> DynamicList:
        values = DynamicList()
        st : NodeT= self.find_price(x)

        cur_prod : Product = st.key

        while st is not None and (cur_prod.price < y or cur_prod.price == y):
            values.pushBack(cur_prod)
            st = self.tree_data.next(st)
            try:
                cur_prod = st.key
            except Exception as nullNode:
                pass
        return values
    
    def rangeSearch_json(self, x:int, y:int) -> list:
        values = []
        st : NodeT= self.find_price(x)

        cur_prod : Product = st.key

        while st is not None and (cur_prod.price < y or cur_prod.price == y):
            values.append(cur_prod.json())
            st = self.tree_data.next(st)
            try:
                cur_prod = st.key
            except Exception as nullNode:
                pass
        return values

    def filterGreater(self,price:int) -> str:
        max : Product = self.tree_data.max().key
        max_price : int = max.price
        filter : DynamicList = self.rangeSearch(price,max_price)
        return str(filter)
    
    def filterGreater_json(self,price:int) -> list:
        max : Product = self.tree_data.max().key
        max_price : int = max.price
        filter : list = self.rangeSearch_json(price,max_price)
        return filter
        
    def filterLower(self,price : int) -> str:
        min : Product = self.tree_data.min().key
        min_price : int = min.price
        filter : DynamicList = self.rangeSearch(min_price,price)
        return str(filter)
    
    def filterLower_json(self,price : int) -> list:
        min : Product = self.tree_data.min().key
        min_price : int = min.price
        filter : list = self.rangeSearch_json(min_price,price)
        return filter
    
    def filter(self,price_min : int ,price_max: int) -> str:
        filter : DynamicList = self.rangeSearch(price_min,price_max)
        return str(filter)
    
    def filter_json(self,price_min : int ,price_max: int) -> list:
        filter : list = self.rangeSearch_json(price_min,price_max)
        return filter
    
    def preOrderCall_JSON(self, ptr:NodeT, result:list) -> list:
        if ptr is None:
            return result
        else:
            result.append(ptr.key.json())
            result = self.preOrderCall_JSON(ptr.left,result)
            result = self.preOrderCall_JSON(ptr.right, result)
            return result

    def preOrder_JSON(self) -> list:
        result = []
        return self.preOrderCall_JSON(self.tree_data.root, result)

    def view_results(self) -> list:
        return self.preOrder_JSON()
    

    def inOrderCall_JSON(self, ptr:NodeT, result:list) -> list:
        if ptr is None:
            return result
        else:
            result = self.inOrderCall_JSON(ptr.left, result)
            result.append(ptr.key.json())
            result = self.inOrderCall_JSON(ptr.right, result)
            return result

    def inOrder_JSON(self) -> list:
        result = []
        return self.inOrderCall_JSON(self.tree_data.root, result)
    
    def view_results_order(self) -> list:
        return self.inOrder_JSON()
    
    def inOrderCallInv_JSON(self, ptr:NodeT, result:list) -> list:
        if ptr is None:
            return result
        else:
            result = self.inOrderCallInv_JSON(ptr.right, result)
            result.append(ptr.key.json())
            result = self.inOrderCallInv_JSON(ptr.left, result)
            return result

    def inOrderInv_JSON(self) -> list:
        result = []
        return self.inOrderCallInv_JSON(self.tree_data.root, result)
    
    def view_results_orderInv(self) -> list:
        return self.inOrderInv_JSON()

def results_AVL_imp():
    myImplementation = ResultsAVL("src/productos.csv")
    return myImplementation