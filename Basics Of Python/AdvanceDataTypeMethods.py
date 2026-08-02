li1 = list('kod')
print(li1) #['k', 'o', 'd']

li2 = list((10,20))
print(li2) #[10, 20]

li3 = list({100, 200})
print(li3) #[200, 100]

li4 = list({'Name':'Priya', 'Age':'27'})
print(li4) #['Name', 'Age']

li5 = list(range(1,11))
print(li5) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#tuple(iterable_object)
tup1 = tuple([10,20,30])
print(tup1) #(10, 20, 30)
tup2 = tuple([100,200])
print(tup2) #(100, 200)
tup3 = tuple(range(1,11))
print(tup3) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup4 = tuple('Kodnest')
print(tup4) #('K', 'o', 'd', 'n', 'e', 's', 't')
tup5 = tuple({'name':'prashi','Age':22})
print(tup5) #('name', 'Age')

#Set(iterable_object)
S1 = set([10,20,20,30])
print(S1) #{10, 20, 30}

#dict(iterable_object:key:value)
d1 = dict([['name','Priya'], ['age',22]])
print(d1) #{'name': 'Priya', 'age': 22}
