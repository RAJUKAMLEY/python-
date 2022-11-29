string = input("enter the string")
if (string==string[::-1]):
    print("palindrome")
else:
    print("not palindrome")    
    
    
#prime
prime=int(input("enter the number"))
if prime>1:
    for i in range(2, prime):
        if (prime%i)==0:
            print ( "not prime")
            break
        else:
            print( "is prime")    
else:
    print("is not a prime")