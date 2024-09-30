import math

m,n,a = map(int,input().split())
v = math.ceil(m/a)
h = math.ceil(n/a)
print(v*h)