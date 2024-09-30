tc = int(input())
for _ in range(tc):
    n = int(input())
    l = list(map(int,input().split()))
    sum = 0
    for i in range(0,n):
        if i%2:
            sum-=l[i]
        else:
            sum+=l[i]
    print(sum)