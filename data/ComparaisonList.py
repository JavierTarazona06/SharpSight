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
                                     link=self.lector['link'][i])
                self.list.pushBack(curProduct)
        else:
            with open("src/comparisonList.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'price', 'link'])

    def insert(self, prod: Product):
        self.list.pushFront(prod)
        df = pd.read_csv("src/comparisonList.csv")
        rows = df.shape[0]
        data = pd.DataFrame({"title": prod.title, "price": prod.price, "link": prod.link}, index=[rows])
        df = pd.concat([df, data])
        df.to_csv("src/comparisonList.csv", index=False)

    def delete(self, index):
        prod = self.list.list[index]
        print(self.list.deleteIndex(index))
        df = pd.read_csv("src/comparisonList.csv")
        df = df.drop(index)
        df.to_csv("src/comparisonList.csv", index=False)
        print("Deleted from wish list: " + str(prod))

    def __str__(self):
        if self.list.empty():
            return ""
        elif self.list.size == 1:
            prod = self.list.list[0]
            return str(prod.title) + " " + str(format(prod.price, ',')) + " " + str(prod.link)
        else:
            list = ""
            a = 0
            for i in range(0, self.list.index - 1):
                prod = self.list.list[i]
                list += str(prod.title) + " " + str(format(prod.price, ',')) + " " + str(prod.link) + "\n"
                a = i
            prod = self.list.list[a + 1]
            list += str(prod.title) + " " + str(format(prod.price, ',')) + " " + str(prod.link)
            return list

    def strListProd(self,lista):
        if lista.empty():
            return ""
        elif lista.size == 1:
            prod = lista.list[0]
            return str(prod.title) + " " + str(format(prod.price, ',')) + " " + str(prod.link)
        else:
            listy = ""
            a = 0
            for i in range(0, lista.index - 1):
                prod = lista.list[i]
                listy += str(prod.title) + " " + str(format(prod.price, ',')) + " " + str(prod.link) + "\n"
                a = i
            prod = lista.list[a + 1]
            listy += str(prod.title) + " " + str(format(prod.price, ',')) + " " + str(prod.link)
            return listy

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
        returning += self.strListProd(listSortedPrice)
        return returning