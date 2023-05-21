# 時間太長
while(True):
    x, y = map(int, input().split())
    if x==0 and y==0:
        break
    dic = {}
    if x>y:
        temp = x
        x = y
        y = temp
    for i in range(x, y+1):
        i = str(i)
        for j in range(len(i)):
            dic[int(i[j])] = dic.get(int(i[j]), 0)+1
    for i in range(10):
        print(dic[i], end = ' ')
    print()