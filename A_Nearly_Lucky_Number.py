lucky = ["4","7"]
n = input()
cnt = 0
for ch in n:
    if ch in lucky:
        cnt+=1
print("YES" if str(cnt) in lucky else "NO")