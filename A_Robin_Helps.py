tc = int(input())

for _ in range(tc):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    goldCount = 0
    cnt = 0
    for e in range(n):
        if a[e] == 0 and goldCount>0:
            goldCount-=1
            cnt+=1
        if a[e] >= k:
            goldCount+=a[e]
    print(cnt)
