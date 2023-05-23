from data.ComparaisonList import ComparisonList

#from SharpSight.data.Node import *
from data.WishList import WishList
#from WishList import *
from data import Results
#from data import Results
from Scrapping import Search


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
        print("7. Save in wish list")
        print("8. Save in compare list")
        print("9. Close")
        try:
            n = int(input())
            if not (n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7 or n == 8 or n == 9):
                print("Número incorrecto")
            elif n == 1:
                print(resImplem)
            elif n == 2:
                resImplem.orderListPrice()
                print(resImplem)
            elif n == 3:
                resImplem.orderListPriceReverse()
                print(resImplem)
            elif n == 4:
                print(resImplem.bestProduct())
            elif n==5:
                flag2=False
                print("Insert value to filter Greater")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                if flag2:
                    resImplem.filterGreater(num)
                    print(resImplem)
            elif n==6:
                flag2=False
                print("Insert value to filter Lower")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                if flag2:
                    resImplem.filterLower(num)
                    print(resImplem)
            elif n==7:
                flag2=False
                print("Insert index of product to save:")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                if flag2:
                    wish = WishList()
                    prodWished = resImplem.list_data.getNode(num).key
                    wish.insert(prodWished)
                    print("Inserted in wish list: "+str(prodWished))
            elif n==8:
                flag2=False
                print("Insert index of product to save:")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                if flag2:
                    comp = ComparisonList()
                    prodToComp = resImplem.list_data.getNode(num).key
                    comp.insert(prodToComp)
                    print("Inserted in compare list: "+str(prodToComp))
            else:
                print("Goodbye\n")
                flag = False
        except Exception as e:
            print("Not a number!!\n")
            print(e)


def menuSearchProducts():
    flag = True
    while flag:
        print("Insert a product name:")
        keyProd = input()
        Search.Search(keyProd)
        resImplem = Results.generalResultsImplementation()
        print("Data loadaded")
        print("What do you want to do:")
        print("1. See list of products")
        print("2. Order products")
        print("3. Order products in reverse")
        print("4. Best product")
        print("5. Filter Greater")
        print("6. Filter Lower")
        print("7. Save in wish list")
        print("8. Save in compare list")
        print("9. Close")
        try:
            n = int(input())
            if not (n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7 or n == 8 or n == 9):
                print("Número incorrecto")
                menuProductsSaved(resImplem)
                flag=False
            elif n == 1:
                print(resImplem)
                menuProductsSaved(resImplem)
                flag=False
            elif n == 2:
                resImplem.orderListPrice()
                print(resImplem)
                menuProductsSaved(resImplem)
                flag=False
            elif n == 3:
                resImplem.orderListPriceReverse()
                print(resImplem)
                menuProductsSaved(resImplem)
                flag=False
            elif n == 4:
                print(resImplem.bestProduct())
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
                    menuProductsSaved(resImplem)
                    flag = False
                if flag2:
                    resImplem.filterGreater(num)
                    print(resImplem)
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
                    menuProductsSaved(resImplem)
                    flag = False
                if flag2:
                    resImplem.filterLower(num)
                    print(resImplem)
                    menuProductsSaved(resImplem)
                    flag = False
            elif n==7:
                flag2=False
                print("Insert index of product to save:")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                    menuProductsSaved(resImplem)
                    flag = False
                if flag2:
                    wish = WishList()
                    prodWished = resImplem.list_data.getNode(num).key
                    wish.insert(prodWished)
                    print("Inserted in wish list: "+str(prodWished))
                    menuProductsSaved(resImplem)
                    flag = False
            elif n==8:
                flag2=False
                print("Insert index of product to save:")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                    menuProductsSaved(resImplem)
                    flag = False
                if flag2:
                    comp = ComparisonList()
                    prodToComp = resImplem.list_data.getNode(num).key
                    comp.insert(prodToComp)
                    print("Inserted in compare list: "+str(prodToComp))
                    menuProductsSaved(resImplem)
                    flag = False
            else:
                print("Goodbye\n")
                flag = False
        except:
            print("Not a number!!\n")
            menuProductsSaved(resImplem)
            flag = False

def menuWishList():
    flag = True
    while flag:
        print("Select an option:")
        print("1. View wish list")
        print("2. Delete last element in wish list")
        print("3. Close")
        try:
            n = int(input())
            if not(n==1 or n==2 or n==3):
                print("Número incorrecto")
            elif n==1:
                wishList = WishList()
                print(wishList)
            elif n==2:
                wishList = WishList()
                try:
                    wishList.delete()
                except:
                    print("The wish list is empty!!\n")
            else:
                print("Goodbye\n")
                flag = False
        except:
            print("Not a number!!\n")

def menuComparisonList():
    flag = True
    while flag:
        print("Select an option:")
        print("1. View comparison list")
        print("2. Compare by price")
        print("3. Delete an element")
        print("4. Close")
        try:
            n = int(input())
            if not(n==1 or n==2 or n==3 or n==4):
                print("Número incorrecto")
            elif n==1:
                comparison = ComparisonList()
                print(comparison)
            elif n==2:
                comparison = ComparisonList()
                print(comparison.compareByPrice())
            elif n==3:
                comparison = ComparisonList()
                flag2=False
                print("Insert index of product to delete:")
                num = -1
                try:
                    num = int(input())
                    flag2=True
                except:
                    print("Num is not integer")
                if flag2:
                    try:
                        comparison.delete(num)
                    except Exception as e:
                        print("The comparison list is empty or wrong index!!\n")
                        print(e)
            else:
                print("Good bye\n")
                flag = False
        except Exception as e:
            print("Not a number!!\n")
            print(e)

def startMenu():
    flag = True
    while flag:
        print("Welcome to Sharp Sight")
        print("What do you want to do today?")
        print("Please select the number:")
        print("1. Search a product")
        print("2. Whish List")
        print("3. Comparison List")
        print("4. Close")
        try:
            n = int(input())
            if not (n == 1 or n == 2 or n == 3 or n == 4):
                print("Número incorrecto")
            elif n == 1:
                menuSearchProducts()
            elif n == 2:
                menuWishList()
            elif n == 3:
                menuComparisonList()
            else:
                print("Goodbye\n")
                flag = False
        except:
            print("Not a number!!\n")