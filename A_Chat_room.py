h = "hello"
w = input().lower()
ptr = 0
for c in w:
    if c==h[ptr]:
        ptr+=1
    if ptr==5:break
print("YES" if ptr==5 else "NO")