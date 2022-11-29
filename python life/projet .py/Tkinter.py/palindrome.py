def ispalindrome (s):
    return s == s[::-1]

#Driver Code 
s = "malayalam"
ans = ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")  
    
    #palindrome pharse number or a sequence will be same even if written in backwards
    
# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")    
    
    
    
    
# Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold() # weather it's a small or capital

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
   
   

def pal(num):
    x1 = num [::-1]
    if x1 == num:
        print("palindrome")
    else:
        print("not a palindrome")
print(pal("madam"))      



def pal(num):
    x1 = num [::-1]
    if x1 == num:
        print("palindrome")
    else:
        print("not a palindrome")
print(pal("raju"))  \
    
    

def pal(num):
    x1 = num [::-1]
    if x1 == num:
        print("palindrome")
    else:
        print("not a palindrome")
print(pal("151"))  