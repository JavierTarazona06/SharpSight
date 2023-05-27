class Product:

    def __init__(self, title : str, price : int, link : str, seller : str):
        self.title = str(title)
        self.price = int(price)
        self.link = str(link)
        self.seller = str(seller)

    def __str__(self):
        return str(self.title) + " $" + str(f"{self.price:,}") + " " + str(self.link) + " " + str(self.seller )
        #return " $" + str(f"{self.price:,}")
        #return str(self.seller)
    
    def json(self) -> dict:
        result = {'titulo':self.title,'precio':self.price,'link':self.link,'tienda':self.seller}
        return result

    def __lt__(self, other_prod):
        return self.price < other_prod.price

    def __le__(self, other_prod):
        return self.price <= other_prod.price

    def __eq__(self, other_prod):
        return (self.price == other_prod.price) and (self.title == other_prod.title) and (self.link == other_prod.link) and (self.seller == other_prod.seller)
        #return (self.price == other_prod.price) 

    def __gt__(self, other_prod):
        return self.price > other_prod.price

    def __ge__(self, other_prod):
        return self.price >= other_prod.price

    def compare_title(self, other_prod):
        if self.title > other_prod.title:
            return 1
        elif self.title == other_prod.title:
            return 0
        else:
            return -1

    def compare_seller (self, other_prod):
        if self.seller  > other_prod.seller :
            return 1
        elif self.seller  == other_prod.seller :
            return 0
        else:
            return -1