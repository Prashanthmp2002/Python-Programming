'''
1. Once we declare the string we cannot modify, 
if we try to modify the string it will create new string

2. If new string does not have any refernce variable then it will be remove

3. python internally uses string Interning

4. String interning is the process of checking string intern poll before creating any new object

5. when ever we want to create new object, python first will check intern intern poll, weather that object already  exist or not.

6. when Object already exist in the string intern records then address of existing objuct will be resued.
'''
#s1 = 'Kodnest'
#s2 = s1.upper()
#print(s2)

#s1 = 'k'
#print(s1, id(s1))

s1 = 'Hello'
s2 = 'world'

print(s1, id(s1))
print(s2, id(s2))

print('s1 ID of H :',id(s1[0])) 
print('s2 ID of W :',id(s2[0])) 

print('s1 ID of o :',id(s1[-1])) 
print('s2 ID of o :',id(s2[1])) 

print('s1 ID of l :',id(s1[2])) 
print('s1 ID of l :',id(s1[3])) 
print('s2 ID of l :',id(s2[3])) 