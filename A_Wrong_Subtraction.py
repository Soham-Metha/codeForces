n,k = input().split()
i = 0
k = int(k)
while i<k:
    if n[-1]=="0":
        n = n[:-1]
    else:
        n = str(int(n)-1)
    i+=1

print(n)