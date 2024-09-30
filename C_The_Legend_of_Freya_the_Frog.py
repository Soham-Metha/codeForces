import math as m
tc = int(input())

for _ in range(tc):
    x,y,k = map(int,input().split())
    
    stepsInX= m.ceil(x/k)
    stepsInY= m.ceil(y/k)
    diff = abs(stepsInX-stepsInY)
    
    if stepsInX>=stepsInY:diff=max(diff-1,0)
    
    print(stepsInX+stepsInY+diff)