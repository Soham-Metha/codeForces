n,k = map(int,input().split())
l = list(map(int,input().split()))

def cmp(n,k,l):
    if l[0]<1:
        return -1
    
    while l[k]<1:
        k-=1
    
    if l[n]==l[k]:
        return n
    
    while l[k]==l[k+1]:
        k+=1

    return k

print(cmp(n-1,k-1,l)+1)