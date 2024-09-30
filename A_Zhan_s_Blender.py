import math
def cmp(c,x,y):
    res = 0
    if c==0:
        return 0
    if c<x and c<y:
        return 1
    if x>y:
        res = math.ceil(c/y)
    else:
        res = math.ceil(c/x)
        
    return res

tc = int(input())
for i in range(tc):
    fruitsC = int(input())
    x,y = map(int,input().split())
    print(cmp(fruitsC,x,y))
