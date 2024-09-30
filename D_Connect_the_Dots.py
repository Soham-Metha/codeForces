tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    cnt = 0
    r = []
    for i in range(n):r.append(i+1)
    r = set(r)
    for _ in range(m):
        
        res = []
        a,d,k = map(int,input().split())
        tmp = a
        
        for i in range(k+1):
            res.append(tmp)
            tmp+=d
            
        b = True
        for i in res:
            if i not in r:
                b = False
                break
        if b : cnt+=1
         
        for i in res:
            if i in r:
                r.remove(i)
                
    print(len(r)+cnt)