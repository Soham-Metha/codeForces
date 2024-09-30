s = input().lower()

for ch in s:
    if ch not in "aeiouy":
        print("."+ch,end="")
    