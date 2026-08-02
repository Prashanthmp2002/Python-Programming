'''
1. We can store Homogeneous as well as Heterogeneous Data.
2. In list we can store the duplicate values.
3. List is an Order collection of Data: Order of insertion will remain 
    as it is in output.
4. List are Mutable: Once  we declare the list we can modify it.
'''
li1 = [10,20,45,True,'Kodnest',20]
print(li1,type(li1))

#append(): Will add element at the end of the list
li1.append(300)
print(li1) #[10, 20, 45, True, 'Kodnest', 20, 300]

#insert(index,element):
li1.insert(1,15)
print(li1) #[10, 15, 20, 45, True, 'Kodnest', 20, 300]

#remove(ele): Remove the first Occurrence of the specified ele.
li1.remove(20)
print(li1) #[10, 15, 45, True, 'Kodnest', 20, 300]

#in and not in Operator: adds an ele. at specified index
print(2000 in li1) #False
print('Kodnest' in li1) #true

#pop(): Without argument will delete and return last ele. from list
removed_ele = li1.pop()
print(removed_ele) #300
print(li1) #[10, 15, 45, True, 'Kodnest', 20]

#pop(): with argument will delete the ele. at specified index
removed_ele = li1.pop(4)
print(removed_ele) #Kodnest
print(li1) #[10, 15, 45, True, 20]

#del keyword:
#li1.pop()
del li1[1]
print(li1) #[10, 45, True, 20]

del li1 #name 'li1' is not defined
#print(li1)