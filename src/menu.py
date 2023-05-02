from src import productos
from data import Results


def menuProductsSaved(resImplem):
    flag = True
    while flag:
        print("Select an operation over de data previously loaded:")
        print("1. See list of products")
        print("2. Order products")
        print("3. Order products in reverse")
        print("4. Best product")
        print("5. Filter Greater")
        print("6. Filter Lower")
        print("7. Close")
        n = int(input())
        if not (n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7):
            print("Número incorrecto")
        elif n == 1:
            print(resImplem.list_data.strProductList())
        elif n == 2:
            resImplem.orderListPrice()
            print(resImplem.list_data.strProductList())
        elif n == 3:
            resImplem.orderListPriceReverse()
            print(resImplem.list_data.strProductList())
        elif n == 4:
            print(resImplem.bestProduct().strProductList())
        elif n==5:
            flag2=False
            print("Insert value to filter Greater")
            num = -1
            try:
                num = int(input())
                flag2=True
            except:
                print("Num is not integer")
                flag = False
            if flag2:
                resImplem.filterGreater(num)
                print(resImplem.list_data.strProductList())
        elif n==6:
            flag2=False
            print("Insert value to filter Lower")
            num = -1
            try:
                num = int(input())
                flag2=True
            except:
                print("Num is not integer")
                flag = False
            if flag2:
                resImplem.filterLower(num)
                print(resImplem.list_data.strProductList())
        else:
            print("Good bye")
            flag = False


def menuSearchProducts():
    flag = True
    while flag:
        print("Insert a product name:")
        keyProd = input()
        productos.searchProduct(keyProd)
        resImplem = Results.generalResultsImplementation()
        print("Data loadaded")
        print("What do you want to do:")
        print("1. See list of products")
        print("2. Order products")
        print("3. Order products in reverse")
        print("4. Best product")
        print("5. Filter Greater")
        print("6. Filter Lower")
        print("7. Close")
        n = int(input())
        if not (n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7):
            print("Número incorrecto")
        elif n == 1:
            print(resImplem.list_data.strProductList())
            menuProductsSaved(resImplem)
            flag=False
        elif n == 2:
            resImplem.orderListPrice()
            print(resImplem.list_data.strProductList())
            menuProductsSaved(resImplem)
            flag=False
        elif n == 3:
            resImplem.orderListPriceReverse()
            print(resImplem.list_data.strProductList())
            menuProductsSaved(resImplem)
            flag=False
        elif n == 4:
            print(resImplem.bestProduct().strProductList())
            menuProductsSaved(resImplem)
            flag=False
        elif n==5:
            flag2=False
            print("Insert value to filter Greater")
            num = -1
            try:
                num = int(input())
                flag2=True
            except:
                print("Num is not integer")
                flag = False
            if flag2:
                resImplem.filterGreater(num)
                print(resImplem.list_data.strProductList())
                menuProductsSaved(resImplem)
                flag = False
        elif n==6:
            flag2=False
            print("Insert value to filter Lower")
            num = -1
            try:
                num = int(input())
                flag2=True
            except:
                print("Num is not integer")
                flag = False
            if flag2:
                resImplem.filterLower(num)
                print(resImplem.list_data.strProductList())
                menuProductsSaved(resImplem)
                flag = False
        else:
            print("Good bye")
            flag = False


def startMenu():
    flag = True
    while flag:
        print("Welcome to Sharp Sight")
        print("What do you want to do today?")
        print("Please select the number:")
        print("1. Search a product")
        print("2. Whish List")
        print("3. Cerrar")
        n = int(input())
        if not (n == 1 or n == 2 or n == 3):
            print("Número incorrecto")
        elif n == 1:
            menuSearchProducts()
        elif n == 2:
            # whishList()
            pass
        else:
            print("Good bye")
            flag = False


startMenu()
