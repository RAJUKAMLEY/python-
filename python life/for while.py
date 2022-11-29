#for & while looping
# it will rorate like circle when we said then it will stop
from asyncio import locks
import traceback


for i in range(1,10): # i is temperare storage
    print(i)


#
b = "raju"
for i in b:
    print(i) 
    
l=["a","b","c"]
for i in l:
    print(i)    

l=[1,2,3,4,5,5]#in for loop we can if condition also
for r in l:
    if r==1:
        print(l)
    else:
        print(l)        
        
#while loop
#we have to write keyword while
#while True:
    #print ("this") infinite loop because is it's true
    
#example
#without infinite method
c=0
while c<3:# c=0<3 it's true 1<3 true 2<3 true 3<3 false
    c=c+1   # c=0+1=1 1+1=2 2+1=3 
    print("eholr")
else:
    print("op")   # in while condition if the statement is true means it will take until true come


for i in 'raju':     #we can use list , set , tulpe , dict ,strings
    print(i)
    
    
r =[9,6,3,1,4,7]    # list
for i in r:
    print(i)
    
# sum  
r =[9,6,3,1,4,7]# list
sum=0
for i in r:
    sum=sum+1
    print(sum)
    
    
r =[9,6,3,1,4,7]
sum=0
for i in r:
    sum=sum+i
    print(sum)
    
    
for i in range(1,100):
    print(i)  
      
for i in range (1 , 99 , 9): # step size to increment
    print(i)
    
    
    
for i in range(0,45,-5):
    print (i)
    
    
mobiles=['iphone','iqqq','redmi','realme']
for i in mobiles:
    if i=='iqqq':
        print('this is iqq')
    else:
        print('this not ')
        
        
        
c=0
while c>9: # we false the while condition to run else
    c+=1
    print("c")
else:
    print('f')
    
    
    