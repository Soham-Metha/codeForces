t = int(input())
for _ in range(t):
    s = list(input())
    t = input()
    l1,l2 = len(s),len(t)
    ptr1,ptr2 = 0,0
    while ptr1 < l1 and ptr2 < l2:
        if s[ptr1] == '?': 
            s[ptr1] = t[ptr2]
        if s[ptr1] == t[ptr2]: ptr2+=1
        ptr1+=1
        
    if ptr2 == l2:
        print("YES")
        
        for a in s:
            if a=="?":print("a",end="")
            else:print(a,end="")
            
        print()
    else:
        print("NO")