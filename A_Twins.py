n = int(input())
l = sorted(list(map(int,input().split())))
presum = [0]
for i in l:
    presum.append(presum[-1]+i)
for i in reversed(range(n+1)):
    if presum[i] < presum[-1]-presum[i]:
        print(n-i)
        break