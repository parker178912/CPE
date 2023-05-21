while(True):
    x = int(input())
    sum = 0
    i = 1
    if x==0:
        break
    while(True):
        if x==1:
            print(2,2)
            break
        if sum<x:
            sum = sum + i
            i = i+1
        if sum==x:
            print(i,i)
            break
        if sum>x:
            print(sum-x,i-1)
            break