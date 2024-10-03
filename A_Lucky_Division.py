n = input()
l = set(n)=={'4','7'}
s = True
n=int(n)
for i in range(n+1):
    if (set(str(i)).issubset({'4','7'}) and n%i == 0) or l:
        print("YES")
        s = False
        break
if s:
    print("NO")