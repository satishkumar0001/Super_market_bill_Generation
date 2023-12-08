#Bill Generation
print(8*" ", "WELCOME TO CLOTHING AND ACCESORIES")
Username=input("Enter your Name: ")
#Creating a list of items
List_of_items='''
Shirt      : 1000 Rs/piece
Pant       : 1000 Rs/piece
Jacket     : 2500 Rs/piece
Watch      : 1000 Rs/piece
Sunglasses : 500  Rs/piece
Perfume    : 200  Rs/bottle
Shoes      : 1500 Rs/pair'''

#Decleration
Price=0
Totalprice=0
Finalprice=0
Pricelist=[]
Itemslist=[]
Quantitylist=[]
Price_list=[]

#Creating a keys and values in Dictionary

Items_in_shop={'Shirt':1000, 'Pant':1000, 'Jacket':2500, 'Watch':1000, 
'Sunglasses':500, 'Perfume':200, 'Shoes':1500}

user=int(input("For list of items press 1: "))
if user==1:
    print(List_of_items)
else:
    print("Enter a valid input")
    
for i in range(len(Items_in_shop)):
    user=int(input("If you want to buy press 1 and press 2 for exit: "))
    if user==2:
        break
    else:
        if user==1:
                items=input("Which item do you want: ")
                Quantity=int(input("How many do you want: "))
                if items in Items_in_shop.keys():
                    Price=Quantity*(Items_in_shop[items])
                    Pricelist.append((Items_in_shop,Quantity,items,Price))
                    Totalprice+=Price
                    Itemslist.append(items)
                    Quantitylist.append(Quantity)
                    Price_list.append(Price)
                    Finalprice=Totalprice
                else:
                    print("Sorry this item is not available with us")
        else:
            print("Please enter a correct input")
            
        user=input("Redirecting to payment page--> yes or no:")
        if user=='yes':
            pass
        
if Finalprice!=0:
    print(8*"-", "Clothings and Accesories", 8*"-")
    print(10*" ", "Hyderabad 500018")
    print("Name:", Username)
    print(42*"-")
    print("S.no", 3*" ", "Items", 3*" ", "Quantity", 3*" ", "Price")
    print(42*"-")
    for i in range(len(Pricelist)):
        print(i, 8*" ", Itemslist[i],8*" ", Quantitylist[i],8*" ", Price_list[i])
print(42*"-")
print(17*" ", "GST Amount:", "Rs:-", Totalprice*5/100)
print(16*" ", "Total Amount:", "Rs:-", Totalprice)
print(42*"-")
print(16*" ", "Final Amount:", "Rs:-", Totalprice+Totalprice*5/100)
print(42*"-")
print(8*" ", "Please Vist Again")
print(12*" ", "Thank You")
print(42*"-")