n = int(input())
l = list(map(int,input().split()))
cnt = 1
mx = 1
for i in range(1,n):
    if l[i]>=l[i-1]:
        cnt+=1
        mx = max(mx,cnt)
    else:
        cnt=1
print(mx)