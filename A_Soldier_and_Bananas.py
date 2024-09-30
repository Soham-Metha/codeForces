k,n,w = map(int,input().split())
sm = 0
for i in range(w):
    sm += k*(i+1)

op = (sm-n) if sm>n else 0
print(op)