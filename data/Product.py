class Product:

    def __init__(self, title : str, price : int, link : str, brand : str):
        self.title = title
        self.price = price
        self.link = link
        self.brand = brand

    def __str__(self):
        return str(self.title) + " $" + str(f"{self.price:,}") + " " + str(self.link) + " " + str(self.brand)

    def __lt__(self, other_prod):
        return self.price < other_prod.price

    def __le__(self, other_prod):
        return self.price <= other_prod.price

    def __eq__(self, other_prod):
        return self.price == other_prod.price

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

    def compare_brand(self, other_prod):
        if self.brand > other_prod.brand:
            return 1
        elif self.brand == other_prod.brand:
            return 0
        else:
            return -1