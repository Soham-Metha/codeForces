a = input().lower()
b = input().lower()

n = len(a)

i = 0
op = 0
while i<n:
    if a[i]==b[i]:
        i+=1
    elif a[i]<b[i]:
        op=-1
        break;
    else:
        op=1
        break;

print(op)
        