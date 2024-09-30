tc = int(input())
for _ in range(tc):
    b,c,d = map(int,input().split())
    a = -1
    mx = 2305843009213693952
    for i in range(mx):
        if ((i|b) - (i&c) == d):
            a = i
            break
    
    print(a)
        