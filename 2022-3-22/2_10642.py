time = int(input())
for i in range(time):
    x1, y1, x2, y2 = map(int, input().split())
    sum1 = x1+y1
    sum2 = x2+y2
    insi = 0
    step1 = 0
    step2 = 0
    if sum2-sum1>1:
        for j in range(sum1+1,sum2):
            insi = insi+j
    disp = sum2-sum1
    if sum2-sum1!=0:
        step1 = sum1-x1
        step2 = x2
    else:
        insi = x2-x1
    print("Case %d:"%(i+1),insi+disp+step1+step2)