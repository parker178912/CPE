while(True):
    try:
        x = int(input())
        dic = {}
        for i in range(x):
            key = input()
            value = input()
            dic[key] = value
        y = int(input())
        for i in range(y):
            text = input()
            print(dic[text])
    except:
        break
