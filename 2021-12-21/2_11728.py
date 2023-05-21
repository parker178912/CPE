count = 1
while(True):
    x = int(input())
    temp = 0
    if x==0:
        break
    for i in range(1,x+1):
        sum = 0
        for j in range(1,i+1):
            if i%j==0:
                sum = sum + j
        if sum==x:
            temp = j
    if temp!=0:
        print("Case %d:" %count, temp)
    else:
        print("Case %d: -1"%count)
    count = count + 1