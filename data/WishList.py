from data.Product import Product
from data.QueueDLLT import *
import pandas as pd
import os
import csv


class WishList:
    def __init__(self):
        self.list = QueueDLLT()
        if os.path.exists("src/wishList.csv"):
            self.lector = pd.read_csv("src/wishList.csv")
            for i in range(self.lector.shape[0]):
                curProduct = Product(title=self.lector['title'][i], price=self.lector['price'][i],
                                     link=self.lector['link'][i], brand=self.lector['brand'][i])
                self.list.enqueue(Node(curProduct))
        else:
            with open("src/wishList.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'price', 'link','brand'])

    def __str__(self):
        return str(self.list)

    def insert(self, prod: Product):
        self.list.enqueue(Node(prod))
        df = pd.read_csv("src/wishList.csv")
        rows = df.shape[0]
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link, "brand": prod.brand}, index=[rows])
        df = pd.concat([df, data])
        df.to_csv("src/wishList.csv", index=False)

    def delete(self):
        prod = self.list.first()
        self.list.dequeue()
        df = pd.read_csv("src/wishList.csv")
        df = df.iloc[1:]
        df.to_csv("src/wishList.csv", index=False)
        print("Deleted from wish list: "+str(prod))

'''
myImplementation = generalResultsImplementation()
print(myImplementation.list_data.strProductList())
myImplementation.orderListPrice()
print(myImplementation.list_data.strProductList())
wish = WishList()
prodWished = myImplementation.list_data.getNode(0).key
wish.insert(prodWished)
print("Inserted in wish list: " + str(prodWished))
wish.delete()
wish.delete()
wish.delete()
wish.delete()

wish = WishList()
print(wish.list.strProductList())
'''