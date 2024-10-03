n = int(input())
l = list(map(int,input().split()))
e,o = 0,0
le,lo = 0,0
for i in range(n):
    if l[i]%2: 
        o+=1
        lo=i
    else: 
        e+=1
        le=i
    
    if o==1 and e>1:
        print(lo+1)
        break
    elif e==1 and o>1:
        print(le+1)
        break
