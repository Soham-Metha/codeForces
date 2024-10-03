n,m = map(int,input().split())
l = sorted(list(map(int,input().split())))
pre = []
for i in range(n-1,m):
    pre.append(l[i]-l[i-n+1])
print(min(pre))
    