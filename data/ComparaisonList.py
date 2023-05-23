import csv
import os

import pandas as pd

from data.DynamicList import *
from data.Node import Node
from data.Product import Product


class ComparisonList:

    def __init__(self):
        self.list = DynamicList()
        if os.path.exists("src/comparisonList.csv"):
            self.lector = pd.read_csv("src/comparisonList.csv")
            for i in range(self.lector.shape[0]):
                curProduct = Product(title=self.lector['title'][i], price=self.lector['price'][i],
                                     link=self.lector['link'][i], brand=self.lector['brand'][i])
                self.list.pushBack(curProduct)
        else:
            with open("src/comparisonList.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'price', 'link','brand'])

    def insert(self, prod: Product):
        self.list.pushFront(prod)
        df = pd.read_csv("src/comparisonList.csv")
        rows = df.shape[0]
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link, "brand": prod.brand}, index=[rows])
        df = pd.concat([df, data])
        df.to_csv("src/comparisonList.csv", index=False)

    def delete(self, index):
        prod = self.list.list[index]
        df = pd.read_csv("src/comparisonList.csv")
        df = df.drop(index)
        df.to_csv("src/comparisonList.csv", index=False)
        print("Deleted from comparison list: " + str(prod))

    def __str__(self):
        return str(self.list)

    def insertOrderedPrice(self, listToSort, data):
        if listToSort.empty():
            listToSort.pushBack(data)
        elif listToSort.full():
            raise Exception("List is full")
        else:
            i = 0
            while i < listToSort.index and listToSort.list[i].price < data.price:
                i += 1
            for j in range(listToSort.index, i, -1):
                listToSort.list[j] = listToSort.list[j - 1]
            listToSort.list[i] = data
            listToSort.index += 1
        return listToSort

    def sortPrice(self):
        listaSort = StaticList(self.list.size)
        for i in range(self.list.index):
            listaSort = self.insertOrderedPrice(listaSort, self.list.list[i])
        return listaSort

    def compareByPrice(self):
        listSortedPrice = self.sortPrice()
        best = listSortedPrice.topFront()
        worst = listSortedPrice.topBack()
        returning = "According to price...\n"
        returning += "  The best product is: "+str(best)+"\n"
        returning += "  The most expensive product is: " + str(worst) + "\n"
        returning += "--Presenting all the results:\n"
        returning += str(listSortedPrice)
        return returning