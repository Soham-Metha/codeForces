tc = int(input())

for _ in range(tc):
    word = input()
    ln = len(word)
    if ln > 10:
        op = word[0] + str(ln-2)+word[-1]
    else:
        op = word
    print(op)