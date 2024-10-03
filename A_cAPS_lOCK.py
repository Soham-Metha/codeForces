ip = input()

if ip.isupper():
    print(ip.lower())
elif (ip[1:].isupper() or len(ip)==1) and ip[0].islower():
    print(ip[0].upper()+ip[1:].lower())
else:
    print(ip)