t = int(input())
for _ in range(t):
    n,s,m = map(int,input().split())
    start = []
    end = [0]
    maxdiff = 0
    for i in range(n):
        l,r = map(int,input().split())
        start.append(l)
        end.append(r)
        maxdiff = max(start[i]-end[i],maxdiff)
    maxdiff = max(m-end[-1],maxdiff)
    print("YES" if maxdiff>=s else "NO")
    