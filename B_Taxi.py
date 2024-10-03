import math as m
n = int(input())
l = list(map(int,input().split()))
cnt = [0,0,0,0]
for i in l:
    cnt[i-1] +=1
    
    
res = cnt[3]

if cnt[2]>0:
    res += cnt[2]
    cnt[0]-=min(cnt[0],cnt[2])


if cnt[1]%2:
    cnt[0]-=2
    cnt[1]+=1
res+= m.ceil(cnt[1]/2)

if cnt[0]>0:
    res+=m.ceil(cnt[0]/4)
    
print(res)