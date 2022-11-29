'''fibonacci series program in python. series has number in which each number is the
    sum of two preceding number  
      0112356'''
      
      
a = int(input('enter the first number:'))
b = int(input('enter the second number:'))
n = int(input('enter the  number elements:'))
print(a , b , end="0")
while n-2:
    c = a+b
    a = b
    b = c 
    print(c , end = ",")
    n = n-1
    