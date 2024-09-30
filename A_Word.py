s = input()
lc,uc = 0,0
for ch in s:
    if ord(ch)>90:
        lc+=1
    else:
        uc+=1

op = s.lower() if lc>=uc else s.upper()
print(op)