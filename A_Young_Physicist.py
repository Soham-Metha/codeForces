tc = int(input())
s = list(map(int,input().split()))

for i in range(tc-1):
    l = list(map(int,input().split()))
    s[0]+=l[0]
    s[1]+=l[1]
    s[2]+=l[2]
    
print("YES" if s==[0,0,0] else "NO")