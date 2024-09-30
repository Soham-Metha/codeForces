import math as m
a,b = map(int,input().split())
diff = 0
while(a<=b):
    a = 3*a
    b = 2*b
    diff+=1
print(diff)