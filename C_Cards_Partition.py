"""tc = int(input())
for i in range(tc):
    num1,num2 = map(int,input().split())
    l = list(map(int,input().split()))
    sum  = 0
    for i in l:
        sum+=i
    sum+=num2
    print(sum//max(l))"""