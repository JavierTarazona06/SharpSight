class Product:

    def __init__(self, title,price,link):
        self.title = title
        self.price = price
        self.link = link

    def __str__(self):
        return str(self.title) + " " + str(format(self.price, ',')) + " " + str(self.link)