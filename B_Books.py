n,target= map(int,input().split())
l = list(map(int,input().split()))
precomputed = [0] * (n+1)
    


def binarySearch(l,n,target,offset):
    i,j = 0,n-1
    mid = int((i+j)/2)
    while(j>=i):
        s = precomputed[mid+1]-precomputed[offset]
        if s==target:
            return mid+1-offset
        if s<target:
            i=mid+1
        elif s>target:
            j=mid-1
        mid = int((i+j)/2)
    return i-offset

for i in range(n+1):
    precomputed[i]=precomputed[i-1]+l[i-1]
maxC = 0
i = 0
while (i<n):
    maxC = max(maxC,binarySearch(l,n,target,i))
    i+=1
print(maxC)