from data.DisjointSet import DisjointSet as dS
from data.ResultsAVL import ResultsAVL
from data.Product import Product

class SetSeller():
    def __init__(self) -> None:
        resulAVL_imp = ResultsAVL("src/productos.csv")
        self.products:list = resulAVL_imp.results_list()
        self.setSellers : dS = dS(len(self.products))
        self.setSellers.make_set()
        self.sellers = {}

        for i in range(len(self.products)):
            cur_prod:Product = self.products[i]
            if not cur_prod.seller in self.sellers:
                self.sellers[cur_prod.seller] = i
            self.setSellers.union(i,self.sellers[cur_prod.seller])

    def products_seller(self, in_seller:str) -> list:
        num_seller = self.sellers[in_seller]
        result = []
        for i in range(len(self.products)):
            cur_num_seller = self.setSellers.find(i)
            if cur_num_seller == num_seller:
                result.append(str(self.products[i]))
        return result
    
    def products_seller_json(self, in_seller:str) -> list:
        num_seller = self.sellers[in_seller]
        result = []
        for i in range(len(self.products)):
            cur_num_seller = self.setSellers.find(i)
            if cur_num_seller == num_seller:
                result.append(self.products[i].json())
        return result

    def sellers_json(self) -> dict:
        sellers = self.sellers.keys()
        result = []
        for seller in sellers:
            result.append(seller)
        return {"tiendas" : result}