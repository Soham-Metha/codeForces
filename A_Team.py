tc = int(input())
op = 0
for _ in range(tc):
    s = sum(map(int,input().split()))
    if s>=2: op+=1
print(op)