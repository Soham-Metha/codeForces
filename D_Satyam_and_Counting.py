tc = int(input())
        
for _ in range(tc):
    n = int(input())
    y0,y1 = set(),set()
    res = 0
    for _ in range(n):
        x,y = map(int,input().split())
        if y: y1.add(x)
        else: y0.add(x)
    
    if not y0 or not y1:
        print(res)
        continue
        
    for i in y0:
        if i in y1:
            res+= n-2
        if i-1 not in y1:
            continue

        c1 = i-2 in y0
        c2 = i+1 in y1
        
        if not c1 and not c2: continue
                    
        res+=int(c1)+int(c2)
    
    print(res)