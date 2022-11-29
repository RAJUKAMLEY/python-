'''factorial of a number say "n" will be all paositive number
less than  or equal to n 
      4!= 4*3*2*1'''
      
      
def fact(num):
    if num == 1:
        return num
    else:
        return num*fact(num - 1)
print(fact(4))    