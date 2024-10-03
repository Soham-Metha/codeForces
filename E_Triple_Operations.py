t = int(input())
P = {}
power = 1
ctr = 0
def findN(n):
    #print(P)
    #print(n)
    for key in P.keys():
        if n >= P[key] and n < P [key+1]:
            return key
    return 0

for _ in range(t):
    l,r = map(int,input().split())
    tmp = l
    ctr = 0
    while tmp!=0:
        tmp//=3
        ctr+=1 # 3**ctr = power
    ctr*=2
    for i in range(l+1,r):
        tmp = i
        while tmp!=0:
            tmp//=3
            ctr+=1
    print(ctr)