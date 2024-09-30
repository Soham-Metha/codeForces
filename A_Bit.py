tc = int(input())
x = 0
for _ in range(tc):
    if input()[1] == '+':
        x+=1
    else:
        x-=1
print(x)