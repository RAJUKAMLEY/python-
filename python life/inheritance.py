# single parent to child, multilevel grandfather=father=son , hierachical one parent=twochild , multiple inheritance 2parent=son
#single inh
'''class Parent:
    def fun1(self):
        print("raju")
class Child(Parent) :
    def fun2(self):
        print("raj")
obj=Child()
obj.fun2()
obj.fun1() '''
 
# multilevel 
class Parent:
    def fun1(self):
        print("raju")
class Child(Parent) :
    def fun2(self):
        print("raj")
class Grandchild:
    def fun3(self):
        print("ra") 
obj=Grandchild()
obj.fun1()
obj.fun2()
obj.fun3()           