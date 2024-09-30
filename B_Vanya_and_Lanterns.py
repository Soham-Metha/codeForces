n,l= map(int,input().split())
lis = list(map(int,input().split()))

def sort(l,n):
    for i in range(1,n):

        for j in range(i-1,-1,-1):
            if (l[j+1]<l[j]): 
                l[j+1],l[j] = l[j],l[j+1]
            else : break

sort(lis,n)
maxDiff = 2 * max(lis[0],l-lis[-1])
for i in range(1,n):
    diff = float(lis[i]-lis[i-1])
    if(maxDiff<diff):
        maxDiff=diff
       
    
print("{:.10f}".format(float((maxDiff/2))))