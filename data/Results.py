import pandas as pd

from data.Product import Product
from data.DoubleLinkedListTail import *


class Results:

    def __init__(self, filePath):
        self.lector = pd.read_csv(f'{filePath}')
        # Creacion
        self.list_data = DoubleLinkedListTail()
        self.insertProducts()

    # Insercion Nodo
    def insertProducts(self):
        for i in range(self.lector.shape[0]):
            curProduct = Product(title=self.lector['titulo'][i], price=self.lector['precio'][i],
                                 link=self.lector['link'][i], seller=self.lector['marca'][i], image=self.lector['imagen'][i], brand=self.lector['empresa'][i])
            self.list_data.pushBack(Node(curProduct))

    def __str__(self):
        return str(self.list_data)


    # Actualizacion
    def orderListPrice(self):
        self.list_data.sort()

    def orderListPriceReverse(self):
        self.list_data.sort()
        self.list_data.reverse()

    def bestProduct(self):
        self.list_data.sort()
        ptr = self.list_data.head
        best = Node(ptr.key)
        bestFix = ptr.key
        listaBest = DoubleLinkedListTail()
        listaBest.pushBack(best)
        ptr = ptr.next
        while ptr is not None and bestFix.price == ptr.key.price:
            listaBest.pushBack(Node(ptr.key))
            ptr = ptr.next
        return listaBest

    def filterGreater(self,price):
        self.list_data.filterPriceGreater(price)

    def filterLower(self,price):
        self.list_data.filterPriceLower(price)

    def get_products_json(self) -> list:
        products : DoubleLinkedListTail = self.list_data
        result = []
        if products.isEmpty():
            return result
        else:
            headRef : Node = products.head
            while headRef.next is not None:
                result.append(headRef.key.json())
                headRef = headRef.next
            result.append(headRef.key.json())
            return result


def generalResultsImplementation():
    myImplementation = Results("src/productos.csv")
    return myImplementation



'''
myImplementation.filterLower(3000000)
print(myImplementation.list_data.strProductList())
'''
'''
myImplementation.orderListPrice()
print(myImplementation.printProduct())
myImplementation.list_data.reverse()
print(myImplementation.printProduct())
bestProd = myImplementation.bestProduct()
print(str(bestProd.title)+" "+str(bestProd.price)+" "+str(bestProd.link))
'''
