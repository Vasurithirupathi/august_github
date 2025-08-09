from datetime import datetime

name=input("Enter your name:")
lists='''
Rice  RS 20/Kg
Sugar RS 30/Kg
Salt  RS 20/Kg
Oil  RS 280/Kg
Paneer RS 110/Kg
maggi  RS 50/Kg
Boost  RS 90 per each 
Colgate  RS 100per each

'''

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#RATES OF ITEMS

items={
    'Rice':20,
    'Sugar': 30,
    'Oil':80,
    'Paneer':110,
    'Maggi':50,
    'Boost':90,
    'Colgate':90 

}

Option=int(input("for list of items press 1:"))
if Option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("You enterd wrong number")
    inp=input("Can i bill the items yes or no:")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","Srinu supermarket",25*"=")
            print(28*" ","Wanaparthy")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
        for i in range(len(pricelist)):
            print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],8*"",plist[i])
        print(75*"-")
        print(50*" ","TotalAmount:",'RS',totalprice)
        print("gst amount",50*" ",'RS',gst)
        print(75*"-")
        print(50*" ",'finalAmount:','RS',finalamount)
        print(75*"-")
        print(1*"-" "Thanks for visiting")
        print(75*"-")