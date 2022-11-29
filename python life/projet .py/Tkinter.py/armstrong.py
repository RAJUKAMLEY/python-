'''armstrong number is such that sum of the cube of all its diagits is equaal to the same number
             153 1**3 + 5**3 +  3**3 '''
             
             
'''num = int(input('enter the number'))
s = 0
temp = num 

def new_func():
    return

while temp > 0:
    c = temp % 10
    s +=c**3
    temp // new_func() 
if num ==s:
    print ('armstrong number')
else:
    print('not armstrong number')'''
    
    
num = int(input("enter the number"))
s = 0
temp = num 
while temp > 0:
     c = temp % 10
     s += c**3
     temp //=10
if num ==s:
     print("yes")
else:
    print("no")         
        
    