tc = int(input())
def eval(k,n):
    if k>n:
        print(n)
        return
    i = n//k
    cnt = 0
    while n>0 and i>=0:
        tmp = k**i
        if tmp<=n:
            n-=tmp
            cnt+=1
        if i>0:i-=1
    print(cnt)
    
    
    
for _ in range(tc):
    n,k = map(int,input().split())
    eval(k,n)
            