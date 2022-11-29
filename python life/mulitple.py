


class Father:
    def fun1(self):
        print("raju")
class Mother:
    def fun2(self):
        print('ravi')
class Child(Father,Mother):
    def fun3(self):
        print('ramu')
obj=Child()
obj.fun1()
obj.fun2()  
obj.fun3()
    
 #super key word    
class F:
    def __init__(self):
        print("raju")
    def fun1(self):
        print("this is ravi") 
class M(F):
    def __init__(self):
        print('ravi')
        super().__init__()
    def fun2(self):
        print("this is tommy")    
        
obj=M()        


        