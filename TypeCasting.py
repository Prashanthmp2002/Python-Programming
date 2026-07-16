#if String is holding integer then it can be converted into int.
a = '30'
print(a, type(a))
b = int(a)
print(b, type(b))

#string to interger conversion not allowed
x = 'Code'
print(x, type(x))
#y = int(x)
#print(y, type(y))

#p = float(input('Enter float type data')) #12.22
#print(p, type(p))

#boll()
q=''
print(q, type(q))
q = bool(q)
print(q, type(q))

'''
1. While converting int to bool for all non zero values we will get true
2. while converting int to bool for 0 and empty strings we will get false   
'''