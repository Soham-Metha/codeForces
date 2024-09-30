tc = int(input())
for _ in range(tc):
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append(s)
    
    for i in range(n-1,-1,-1):
        print(l[i].find("#")+1,end = " ")
    print()