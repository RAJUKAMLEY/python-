#FILE handling
# opening reading line by line checking ...handling
#function to open file
#open() any text.file like 'rjtxt' 
#operation mode write or read
#r=open('rjtxt','read')
#j=read()
#print(j)
#r=open('rjtxt','read')
#j=read()
#print(j)
#modes r , w , a read , write , append 
#to check line by line readline
r=open('raju.txt','r') # read it and send r 
consy=r.read()
print(consy)
r.close()


#write
'''r=open('raju.txt','r') # read it and send r 
consy=r.write('this first function')
print(consy)
r.close()
r=open('raju.txt','r')
consy=r.read()
print(consy)
r.close()'''


r=open('raju.txt','w') # read it and send r 
consy=r.write('css')
print(consy)
r.close()
r=open('raju.txt','r') # read it and send r 
consy=r.read()
print(consy)
r.close()


r=open('raju.txt','a') # read it and send r 
consy=r.write('css')
print(consy)
r.close()
r=open('raju.txt','r') # read it and send r 
consy=r.read()
print(consy)
r.close()


r=open('raju.txt','r') # read it and send r 
consy=r.write('this')
print(consy)
r.close()
r=open('raju.txt','r') # read it and send r 
consy=r.readlines(22)
print(consy)
r.close()






