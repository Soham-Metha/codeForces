yr = int(input())



for i in range(yr+1,9013):
    if len(set(str(i)))==4:
        print(i)
        break