n = int(input())
l = list(map(int,input().split()))
r = [0]*n
for i in range(n):
    r[l[i]-1] = i+1
for i in r:
    print(i,end=" ")
