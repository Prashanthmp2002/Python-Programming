# Dict is mutable
d1 = {'name':'prashi','age':'24','phone':123456789,'age':'29'}
print(d1,type(d1)) #{'name': 'prashi', 'age': '29', 'phone': 123456789} <class 'dict'>


# In dict we cannot store duplicate keys,
d1['name'] = 'Pooja'
print(d1) #{'name': 'Pooja', 'age': '24', 'phone': 123456789}

# In dict we can store duplicate values,
marks = {'Sci':85, 'Maths':85} #Allowed


for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)