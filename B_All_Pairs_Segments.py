"""tc = int(input())
for i in range(tc):
    numPoints,numQueries = map(int,input().split())
    l = list(map(int,input().split()))
    start = []
    end = []
    for i in range(numPoints):
        for j in range(i+1,numPoints):
            start.append(l[i])
            end.append(l[j])
    ln = len(start)
    d = [0] * numPoints
    i = 0
    k = 0
    while k<numPoints-1:
        j = 0
        while j<i:
            if end[j]>=start[i]:
                d[k]+=1
            j+=1
        while i<ln-1 and start[i]==start[i+1]: 
            d[k]+=1
            i+=1
        d[k]+=1
        k+=1
        i+=1
        
    #print(start)
    #print(end)
    print(d)
    l2 = list(map(int,input().split()))
    
        """