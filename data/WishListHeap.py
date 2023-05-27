from data.HeapMin import HeapMin
import pandas as pd
import os
import csv
from data.Product import Product

class WishListHeap:

    def __init__(self) -> None:
        self.list = HeapMin()
        if os.path.exists("src/wishList.csv"):
            self.lector = pd.read_csv("src/wishList.csv")
            for i in range(self.lector.shape[0]):
                curProduct = Product(title=self.lector['title'][i], price=self.lector['price'][i],
                                     link=self.lector['link'][i], brand=self.lector['brand'][i])
                self.list.enqueue(Node(curProduct))