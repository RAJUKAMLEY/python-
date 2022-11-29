#Oops 
'''
1.class and objects ,  blue print object 
2.inheritance  , child class multiply single level
3.polymorphism , many froms compal time
4.abstraction , data hiding
5.encapsulation , blind data methods'''


#Oops concept divided in five types
'''
blueprint of object in class
example class = car #parent
object = car bands like ferrari , skoda , electric'''
# python constructor is defined with __init__()
# python doesn't support multiple constructor in a class i.e no constructor Overloading

'''class Raju:
    print('python')
    def display(self):
        a=10
        b=12
        print(a.b)
obj=Raju()
obj.display()
print(obj.d)'''
       

#---init---
class Mobile:
    def __initi__(self,brand,battery,ram,camera,price): # initi instaliz variables
      self.brand=brand
      self.battery=battery
      self.ram=ram
      self.camera=camera
      self.price=price
    def display(self):
        print("brand:",self.brand) # self we have to excute
        print("battery:",self.battery)
        print("ram:",self.ram)
        print("camera:",self.camera)
        print("price:",self.price) # it will not excute because we did not created object
        #subrationline
        print('---------')
# if we want output as multiply objects
for i in range(5):
    
    obj=Mobile("iqq",'5000mh','12gb','62mp','23000') 
    obj.display()
   #multiply objects 
obj2=Mobile("nothing1",'5000mh','12gb','62mp','23000')     
obj.display()


        #__def__



class Mobile:
    def __init__(self):
        print('this is init')
    def display(self):
        print('this') 
obj=Mobile ()
obj.display()               