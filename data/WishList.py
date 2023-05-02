from data.Product import Product
from data.StackDLLT import *
import pandas as pd
import os
import csv


class WishList:
    def __init__(self):
        self.list = StackDLLT()
        if os.path.exists("src/wishList.csv"):
            self.lector = pd.read_csv("src/wishList.csv")
            for i in range(self.lector.shape[0]):
                curProduct = Product(title=self.lector['title'][i], price=self.lector['price'][i],
                                     link=self.lector['link'][i])
                self.list.push(Node(curProduct))
        else:
            with open("wishList", 'w', newline='') as file:
                writer = csv.writer(file)

                writer.writerow(['title', 'price', 'link'])

    def insert(self, prod: Product):
        self.list.push(Node(prod))
        '''
        df = pd.read_csv("src/wishList.csv")
        rows = df.shape[0]
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link},index=[rows+1])
        #df = pd.DataFrame(data, columns=["title", "price", "link"])
        df = pd.concat([df.loc[:0], data, df.loc[1:]])
        df.to_csv("src/wishList.csv", index=False)
        '''
        df = pd.read_csv("src/wishList.csv")
        rows = df.shape[0]
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link}, index=[rows])
        df = pd.concat([df, data])
        df.to_csv("src/wishList.csv", index=False)

    def delete(self):
        prod = self.list.peek()
        self.list.pop()
        df = pd.read_csv("src/wishList.csv")
        df = df.iloc[:-1]
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