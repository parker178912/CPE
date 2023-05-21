while (1==1):
    I = int(input())
    if I == 0:
        break
    num = I
    string = ""
    count = 0
    while (num > 0):
        string = string + str(num%2)
        if num%2 == 1:
            count = count+1
        if num == 1:
            num = 0
        else:
            num = num//2
    string = "".join(reversed(string))
    print("The parity of",string,"is",count,"(mod 2).")