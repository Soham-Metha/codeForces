n = int(input())
s = 0
if n%2:
    s-=n
    n-=1
tmp = n//2
s += tmp**2
s -= tmp*(tmp-1) 
print(int(s))