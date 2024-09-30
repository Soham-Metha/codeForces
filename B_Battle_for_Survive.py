tc = int(input())
for i in range(tc):
    fighterC = int(input())
    l = list(map(int,input().split()))
    sum = 0
    for j in range(fighterC-2):
        sum+=l[j]
    op = l[-1] - (l[-2]-sum)
    print(op)