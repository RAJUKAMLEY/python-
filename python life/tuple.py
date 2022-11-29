#TUPLE IS A IMMUTABLE
# it's a data structure
# in this  elements cannot change
# tuple we take prathaes(_)
#to define list ()
t=()
print(type('t'))


t=(1,2,3,4,5,6,7,8,9,0)
print()

# membership to check given element is their or not to check in we use'in' word
#repations tuple * 2 tuple +2 reapting
#iteration if take in for loop it reapting for i in t: print(i)
#concetination we can two tuple like t1 & t2
#function are 
#min ,max , sum ,sorted
#min means minimum value we will get op
#max maximum value of a tuple 
#sum sum of tuple op
#sorted if the tuple jumpled it will keep it series line
#in tuple we have keep constart


raju=()
print(type(raju))


raju=(1,44,77,99,66,33,'raj')
print(raju[3]) # index 


raju=(1,44,77,99,66,33,'raj')#reaption
print(raju*2)


raju=(1,44,77,99,66,33)
r=(6,5,4,98,7)
print(raju+r) # concartation

#membership
raju=(1,44,77,99,66,33,)
a=(2,6,4,4,9,70)
print(70 in a)


raju=(1,44,77,99,66,33,)
a=(2,6,4,4,9,70)
for i in a:
    print(i)


raju=(1,44,77,99,66,33,)
print(min(raju))

raju=(1,44,77,99,66,33,)
print(max(raju))

raju=(1,44,77,99,66,33,)
print(sum(raju))


raju=(1,44,77,99,66,33,)
print(sorted(raju))