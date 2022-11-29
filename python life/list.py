# list means its data structure and it will do different types of elements datatypes will stored
# [] iden it will count the index from '0' zero 
#raju = [] empty list if we won't send any values
raju = [1,2,3,4,5,6,7]
print(len(raju))

raju =['ramakrishna']
print(len(raju))
#list types
#append - in a list the element it will add 
#extend - it add another elemnt
#remove - it will remove the element
#insert - it will insert value at anyplace we want
#index  - paritcular element is their at this place
#count  - it will count the repeated values 
raju=[2,3.1,"ramu",True]
raju.append(1)
print(raju)
print(type(raju)) # to check the type

raju = ['red']
raju.extend([18118])
print(raju)

raju =[1 ,'blue','orange']
raju.insert(1 , 'black')
print(raju)
 
raju=[1,2,23,2,2,'ramu',True]
print (raju.count(2))


raju=[1,2,23,2,2,'ramu',True]
print(len(raju))

#pop 
raju=[1,2,23,2,2,'ramu',True]
raju.pop(1)
print(raju) #pop means remove

#reverse
raju=[1,2,23,2,2,'ramu',True] # in rhis we will reversr values
raju.reverse()
print(raju)


#sorting
raju=[1,2,23,2,2,65,87 ,74,9]
raju.sort()
print(raju) # it will range in a numeric method
# small to big in sorting method

# in looping
raju=[1,2,23,2,2,65,87 ,74,9]
for i in raju:
    print('i')

'''raju=[1,2,23,2,2,65,87 ,74,9]
print(raju[3][0])'''
    