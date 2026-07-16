N = int(input())
a, b = 0, 1
for i in range(N):
    a, b = b, b+a
    print(a)
    
   
