while(True):
    x = input()
    if x == "0":
        break
    while len(x)>1:
        sum = 0
        for i in range(int(len(x))):
            sum = sum + int(x[i])
        x = str(sum)
    print(x)