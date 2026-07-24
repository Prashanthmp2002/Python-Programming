li1 = [1,2,3,4,5]
duplicate_li1 = [i for i in li1]

#When you have only if part when write it after for loop.
even = [i for i in li1 if i%2 == 0]
print(even) #[2, 4]
sq_list = [i**2 for i in li1]
print(sq_list) #[1, 4, 9, 16, 25]
new_li1 = [ele+2 for ele in li1]
print(new_li1) #[3, 4, 5, 6, 7]

#When  we have if-else both write  it  before for loop
even_add = ['even' if i%2==0 else 'Odd' for i in li1]
print(even_add) #['Odd', 'even', 'Odd', 'even', 'Odd']

#Multipule for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li) #[10, 20, 30, 40, 50, 60]
