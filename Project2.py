from datetime import datetime
username=input("Enter your name:")

# while True:
#     print("items /n:")
#     print()
list="""
Rice           Rs  1000/5kgs
Sugar          Rs100/4kgs
Tea_poeder     Rs 150/3kgs
Red_gram       Rs 180/8kgs
Milk_packets   Rs 20/1 packets
Curd           Rs 20/2 packets
"""
print(list)
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
itemlist=[]
quantitylist=0
plist=[] #above price list and this different'


#rates for item
items_rates={'Rice':1000,'Sugar':100,'Tea_powder':150, 'Red_gram':80,'Curd':20,'Milk':20}
print(items_rates)

Option=eval(input("Pleass enter your option:"))

if Option==1:
    print(items_rates)
    for i in range(len(items_rates)):
        inp1=eval(input("If you want to buy press 1 or 2 is exit:"))

        if inp1==1:
            print("i exited")
             
            break
        elif inp1==2:
    
            print(items_rates)
            item=input("enter your Items:")
            quantity=int(input("enter your Quatity:"))
            if item in items_rates.keys():
                price=quantity*(items_rates[item])
                pricelist.append((item, quantity, items_rates,price))
                totalprice=totalprice+price
                itemlist.append(item)
                quantitylist.append(quantity)
                plist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice
            else:
                print("not available item")
        else:
            print("no that option number")        


                


                


            





