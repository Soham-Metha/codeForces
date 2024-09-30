n,h = map(int,input().split())
l = list(map(int,input().split()))
w = 0
for i in l:
    if i>h:
        w+=1
    w+=1
print(w)