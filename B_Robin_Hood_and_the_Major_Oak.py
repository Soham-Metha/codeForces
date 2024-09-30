tc = int(input())
def chkseries(start,end):
    if start%2 and end%2:
        return not ((end-start+1)//2)%2
    return ((end-start+1)//2)%2
     
for _ in range(tc):
    n,k = map(int,input().split())
    print("NO" if chkseries(n-k+1,n) else "YES")