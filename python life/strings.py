#strings combination of characters 
# s='a',"a" s1="a" s2="""abc
                    #       def""" we define
#string function are upper() , lower() , split() , count(),replace(),R&Lstrip(),startwith(),endwith(),format()
#mutable
from operator import le


s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(type(s))
print(type(s1))
print(type(s2))

#replace
s='raju'
s1="may i come in"
s2='''
this a logic
'''
a=s2.replace("a","are")
print(a)

#upper
s='raju'
s1="may i come in"
s2='''
this a logic
'''
h=s1.upper()
print(h)

#lower
s='raju'
s1="may i come in"
s2='''
THIS IS LOGICAL
'''
z=s2.lower()
print(z)

#strip
s='raju'
s1="may i come in" #strip eliminate space
s2='''
      this a logic 
'''
y=s2.strip()
print(y)

#split
s='raju'
s1="may i come in"
s2='''
this a logic
'''
p=s1.split()
print(p) #sparating it will be list type 

#startwith
s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(s.startswith('r'))

s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(s1.startswith('a'))


#endwith
s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(s2.endswith('i'))


s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(s1.endswith('n'))

#format
s='raju'
s1="may i come in"
s2='''
this a logic
'''
print('my name is{}'.format(' raju'))

#count
s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(s2.count('i'))

#length
s='raju'
s1="may i come in"
s2='''
this a logic
'''
print(len(s1))





