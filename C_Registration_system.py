t = int(input())
db = {}
for _ in range(t):
    s = input()
    if s not in db:
        db[s]=1
        print("OK")
    else:
        print(s+str(db[s]))
        db[s]+=1