t = int(input())
def spaceship(a,b):
    if a>b: return 1
    elif a==b: return 0
    return -1
for _ in range(t):
    a1,a2,b1,b2 = map(int,input().split())
    a = spaceship(a1,b1) + spaceship(a2,b2) > 0
    b = spaceship(a2,b1) + spaceship(a1,b2) > 0
    
    print((a+b)*2)