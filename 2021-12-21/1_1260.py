time = int(input())
for i in range(time):
    x = int(input())
    y = []
    y = input().split()
    total = 0
    for j in range(x):
        for k in range(j):
            if int(y[j])>=int(y[k]):
                total = total+1
    print(total)