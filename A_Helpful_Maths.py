def insertSort(l:list,n:int):
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if l[j]>l[j+1]: l[j],l[j+1] = l[j+1],l[j]
            else: break


s = input()
ln = len(s)

n = []
for i in range(ln):
    if s[i] in ['1','2','3']:
        n.append(s[i])

insertSort(n,len(n))

op = ""
for num in n:
    op = op + "+" + str(num)

print(op[1:])