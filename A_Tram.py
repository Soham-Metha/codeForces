tc = int(input())
a,b = map(int,input().split())
curr = b
mn = curr

for _ in range(tc-1):
    a,b = map(int,input().split())
    curr-=a
    curr+=b
    if curr>mn: mn = curr
    
print(mn)
    