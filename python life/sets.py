#SETS
#we define sets{}
#set don't take double value 
#set won't have index
#set different element we can send
#{}--dict type {1,3,4}--set
#set function
#add()
#update()
#len()
#pop()
#set oparation
#union
#difference
#interact
#disjoint
#subset
#eg:- 
'''s={1,1,2,3}
   print(s)
   o/p:- 1,2,3'''
   
s={}
print(type(s)) # it will dict beause we didn't pass any elements


s={1,2,3,6,5}
print(type(s)) #it's a set type


#add
s={1,2,12,33,'raju'}
s.add(18)
print(s)


#update
s={1,2,12,33,'raju'}
s.update(['raj'])
print(s)

#remove
s={1,2,12,33,'raju'}
s.remove(1)
print(s)

#length
s={1,2,2,12,33,33,'raju'}

print(len(s))


#union
s1={1,2,12,33,10}
s2={5,6,4,8,8,9,64}
print(s1.union(s2))

#intercation
s1={1,2,12,33,10,8,9}
s2={5,6,4,8,8,9,64}
print(s1.intersection(s2)) # in s2 &s1 what are same number it will only show

#difference
s1={1,2,12,33,10,8,9,6}
s2={5,6,4,8,8,9,64}
print(s1.difference(s2))

#disjoint
s1={1,2,12,33,10}
s2={5,6,4,8,8,9,64}
print(s1.isdisjoint(s2)) # if the elements are not same means true if element are same means false

#subset
s1={1,2,12,33,10}
s2={1,2,12,33,10}
print(s1.union(s2)) # both elements same means true not same means false

















