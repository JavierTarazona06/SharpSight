

import pandas as pd

from AVL import AVL
from Product import Product


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
            self.tree_data.insert(curProduct)