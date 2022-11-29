#function
#baiscs bulid of block
#reuseblity fnction it can work as
#def her def is function key
#function name():
'''  -------- --------
            --------'''
#def raju(app):
  #  print(app)#function call
def raju (raj,course):
    print("this is function",raj,course)
raju('name',1)    


#return
def raju (a,b,c):
    return a+b**c
k=raju(6,8,9)
print(k)   

def raju (a,b,c):
    return a*c
k=raju(6,8,9)
print(k)   

#pass
  # we can pass list tuple

def raju (a):
   for r in a:
       print(r)
raju([1,2,3,4,5]) 

#aruguments 
#mulitple values
'''def raju (a):
    print(a)
raju(1,2,3,4,5,6,7,8,9)'''  #error it will show because positional argument takes 1


def raju (*a):  #we pass star then it will work 
    print(a)  # convert into tuple
raju(1,2,3,4,5,6,7,8,9) 


def raju (**a):
    print(a)
raju(name='raj',age=22) # it will convert into dict
 