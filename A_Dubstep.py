s = input()+"WUB"
n = len(s)
i = 0
words = []
word = ""

while i<n:
    if s[i:i+3]=="WUB":
        i+=2
        if word!="":
            words.append(word)
            word=""
    else:
        word+=s[i]
    i+=1
    
for w in words:
    print(w,end=" ")