"""tc = int(input())
for i in range(tc):
    listLen = int(input())
    list1Max,list2Max = 0,0
    list1Min,list2Min = 10000000001,10000000001
    l = list(map(int,input().split()))
    l1,l2 = [],[]
    len1,len2 = 0,0
    for i in range(listLen):
        if i%2 :
            l1.append(l[i])
            if l1[len1] > list1Max:
                list1Max = l1[len1]
            if l1[len1] < list1Min:
                list1Min = l1[len1]
            len1+=1
        else:
            l2.append(l[i])
            if l2[len2] > list2Max:
                list2Max = l2[len2]
            if l2[len2] < list2Min:
                list2Min = l2[len2]
            len2+=1
    print(max(max(list1Max+list1Min+len1,list2Max+list2Min+len2),))"""