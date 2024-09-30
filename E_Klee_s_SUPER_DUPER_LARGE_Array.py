tc = int(input())
for _ in range(tc):
    n,k = map(int,input().split())
    SumOfSeries = n*(n-1)/2 - (k-1)*(k-2)/2
    halfway = 