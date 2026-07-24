'''
1.In set we can store Homogeneous as well as Heterogeneous Data.
2.Set is an Unorderd Collection Data.
3.Set does not support indexing of data.
4.In Set we cannot store the Duplicates.
5.Sets are Mutable
'''
s1 =  {10, True, 'Kodnest', 10, 20, 55.44}
print(s1, type(s1)) #{True, 20, 55.44, 10, 'Kodnest'} <class 'set'>
#print(s1[0]) #Error

#add
s1.add(500)
print(s1) #{True, 20, 500, 55.44, 10, 'Kodnest'}

#remove
s1.remove(55.44)
print(s1) #{True, 'Kodnest', 20, 500, 10}

#pop  : without index will delete and return one element
poped_ele=s1.pop()
print(poped_ele) #True
print(s1) #{20, 500, 10, 'Kodnest'}

#del s[2] #error
del s1