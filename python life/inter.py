#python program to calculate the length of string
from tkinter import WORD


r="this is the book to read"
#print (len(r))
def length_string(str1):
    count=0
    for i in str1:
        count+=1
    return count
print(length_string(r))     



#python  function that accepts a string to count lowwercase and upper
def string_case(a):
    d={'Upper_case':0 , 'Lower_case':0}
    for i in a :
        if i.isupper():
            d['Upper_case']+=1
        elif i.islower():
            d['Lower_case']+=1
        else:
            pass
    print("Upper case letters:",d['Upper_case'])
    print("lower case letters:",d['Lower_case'])
string_case("Raju Attend The Interview") 


#check if the first and lasst number of a list is the same 
'''number_a = [10,20,30,40,10]
def first_last(number_a):
    first=number_a[0]
    second=number_a[-1]
    print(first,second)
first_last(number_a)   ''' 



number_a = [10,20,30,40,10]
def first_last(number_a):
    first=number_a[0]
    last=number_a[-1]
    if first==last:
        return True
    else:
        return False
print(first_last(number_a))   



#check if a key is already present in a dict
my_dict={1:'a' , 2:'b' , 3:'c'}
if 2 in my_dict:
    print("yes")
else:
    print("no")
    
    
    
#count the occurrance of each word in given sentence
'''def word_count(str):
    counts=dict()
    words=str.split()
    for words in words:
        if WORD in counts:
            counts[words]+=1
        else:
            counts[words] += 1
        return counts
print(word_count("the godfather of the nation"))''' 



#fibonacci 
def fib(m):
    if m==1 or  m==2:
        return 1
    #(n-1)+(n-2)
    else:
        return(fib(m-1)+fib(m-2))
    print(fib(7))
    
    
    #largest number
l=[44,55,66,77,45,107]
print(max(l))


        

        