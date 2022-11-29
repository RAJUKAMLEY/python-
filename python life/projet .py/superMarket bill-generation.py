# super marketing billing
from datetime import datetime
from functools import total_ordering

name=input("enter name:")
#list of iteams
list='''
Rice         Rs20/kg
Sugar        Rs 30/kg
Salt         RS 45/kg
Oil          RS 185/liter
Maggi        Rs 50/pack
Boost        RS 120/each
Ground Nuts  Rs 80/kg
Paneer       Rs 175/kg
Brush        Rs 25/each
Soaps        Rs 45/each'''

# print(list)
# FREE DEFIND DECLARE
# PRICES 
#declaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0 #
ilist=[] 
qlist=[]
plist=[]

#rates for items
# in dict
items={'Rice':40,
       'Sugar':30,'Salt':45,
       'Oil':185,'Maggi':50,'Boost':120,
       'Ground Nuts':80,'Panner':175,'Brush':25,'Soaps':45}
#condition to buy or quit opitions
option=int(input("for list of items press 1:"))

if option==1:
    print(list) # to display items we write the condition
    
for i in range(len(items)): # to buy items
    raj=int(input("if you want to buy press 1 or 2 for exit:"))
    if raj==2:
        break
    if raj==1:
        item=input("enter your items:")
        quantity=int(input("enter qunatity:")) # if the items avaible means it show qunatity
        if item in items.keys():
            price=quantity*(items[item])
#print(price) 
# multiply items
            pricelist.append((item , quantity , items , price )) #  we take it tuple we have to send tuple
            totalprice+=price
            #we append all items
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+price
            #in case we don't have item means
        else:
            print("out_stock")
    else:
        print("entered wrong opition")
        #bill genrate
    raj=input("can i bill the items yes or no:")
    if raj=='yes':
        pass
        if finalamount!=0:
            #effective setting 
            print(25*"=," "BUTTERFLY",25*"=")
            print(28*" ","KURNOOL")
            print("Name:", name,30*" ","Date" , datetime.now)
            print(75*"-")
            print("Sno.",9*" " ,'items.',8*" ",'quantity',3*" " ,'price')
            for i in range(len(pricelist)):
                print(i,8*" ",5*' ' , ilist[i],8*" " , qlist[i] ,8*" " ,plist[i])     
                print(75*"-")
                print(50*" ",'totalamount:' , 'Rs' , totalprice)
                print("gst amounrt",40*" " , 'Rs',gst)
                print(75*"-")
                print(50*" " , 'finalamount:' , 'Rs',finalamount)
                print(75*"-")
                print(20*" ","Thanks for visiting")
                print(75*"-")
                
                    


         
            