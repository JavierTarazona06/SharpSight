import pandas as pd

from data.Product import Product
from data.DoubleLinkedListTail import *


class Results:

    # Procesamiento de datos
    # lector=pd.read_csv(r'C:\Users\Jeison Diaz\OneDrive\Documentos\GitHub\SharpSight\Data_Structures\productosIphone14.csv')
    def __init__(self, filePath):
        self.lector = pd.read_csv(f'{filePath}')
        # Creacion
        self.list_data = DoubleLinkedListTail()
        self.insertProducts()

    # Insercion Nodo
    def insertProducts(self):
        for i in range(self.lector.shape[0]):
            curProduct = Product(title=self.lector['titulo'][i], price=self.lector['precio'][i],
                                 link=self.lector['link'][i])
            self.list_data.pushBack(Node(curProduct))

    # Actualizacion

    def orderListPrice(self):
        self.list_data.sortPrice()

    def orderListPriceReverse(self):
        self.orderListPrice()
        self.list_data.reverse()

    def bestProduct(self):
        self.list_data.sortPrice()
        ptr = self.list_data.head
        best = Node(ptr.key)
        bestFix = Node(ptr.key)
        listaBest = DoubleLinkedListTail()
        listaBest.pushBack(best)
        while ptr.next is not None and bestFix.key.price == ptr.next.key.price:
            listaBest.pushBack(Node(best.next.key))
            ptr = ptr.next
        return listaBest

    def filterGreater(self,price):
        self.list_data.filterPriceGreater(price)

    def filterLower(self,price):
        self.list_data.filterPriceLower(price)

    #def strProduct(self, prod):
        #return str(prod.title) + " " + str(prod.price) + " " + str(prod.link)


def generalResultsImplementation():
    myImplementation = Results("src/productos.csv")
    return myImplementation

'''
myImplementation = generalResultsImplementation()
print(myImplementation.list_data.strProductList())
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
