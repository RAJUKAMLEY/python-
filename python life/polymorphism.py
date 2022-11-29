#polymorphism
#concepts ,class ,objects
'''polymorphism is a concept of object oriented programming , which means multiple forms or more than one from'''
#types , 1. compile-time (method over loading) 2.run-time(a)Method over-riding
#run time or dynamic .different parameters it's from inheritance

#method over-loading
#same class
#same function
#different parameters
#method names
'''class A:
    def sum(self,r,a):
        return r+a
    def sum(self,r,a,b):
        return r+a+b
obj=A()
print(obj.sum(1,2)) '''    # over loding we will get error
'''class A:
    def sum(self,r,a):
        return r+a
    def sum(self,r,a,b=6): # default we have to give
        return r+a+b
obj=A()
print(obj.sum(1,2)) '''


#method over-loading
#different class
#same function
#different parameters
#method names
'''class R:
    def display(self):
        print("the king")
class A:
    def display(self):
        print("the queen")
obj=A()
obj.dispaly()     '''            # we will get only A o/p


class R:
    def display(self):
        print("the king")
class A(R):
    def display(self):
        print("the queen")
        #by using super key
        super().display() 
obj=A()
obj.display()