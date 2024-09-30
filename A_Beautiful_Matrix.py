l = [[],[],[],[],[]]
i,j = 6,6

for n in range(5):
    l[n] = list(map(int,input().split()))
    if 1 in l[n]:
        i = n
        for m in range(5):
            if l[n][m]==1:
                j=m
            
si = abs(2-i)
sj = abs(2-j)
print(si+sj)