'''
1. In tuple we can store Homogeneous as well as Heterogeneous Data.
2. In tuples we can store the Duplicates.
3. Tupels are orderd Collection
4. Tupels are Immutable: Once  we declare the tuple we  cannot modify it.
'''
tup1 = [10, 22.55, 'Kodnest', True,10]
print(tup1) #[10, 22.55, 'Kodnest', True, 10]
#tup1.remove(55)
#tup1.pop()
#del tup1[2]

print(tup1[2])#'kodnest'

#Deletes the comple tup1 object
del tup1
#print(tup1) #Error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)


