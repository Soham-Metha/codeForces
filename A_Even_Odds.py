import math as m
n,k = map(int,input().split())
n2 = m.ceil(n/2)

if k==n:
    last = k-1 if k%2 else k
    print(max(last,1))
    
elif k<=n2:
    print(2*k-1)
    
else:
    print(2*(k-(n2)))