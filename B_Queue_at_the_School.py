n,t = map(int,input().split())
l = list(input())

while(t):
    j = 1
    while j<n:
        if l[j-1] == "B" and l[j] == "G":
            l[j-1],l[j] = "G","B"
            j+=1
        j+=1
    t-=1
            
for i in l:
    print(i,end="")