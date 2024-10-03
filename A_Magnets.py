t = int(input())
l = []
cnt=1
l.append(input())

for _ in range(t-1):
    l.append(input())
    if l[-1][1] != l[-2][1]:
        cnt+=1
print(cnt)