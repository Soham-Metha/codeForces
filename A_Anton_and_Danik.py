n = int(input())
l = list(input())
ac = l.count("A")
dc = n-ac

if ac==dc:
    print("Friendship")
elif ac>dc:
    print("Anton")
else:
    print("Danik")