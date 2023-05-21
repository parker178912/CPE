while(True):
    x = input()
    if x=="-1":
        break
    female = 1
    male = 0
    for i in range(int(x)):
        a = female
        b = male
        female = b+1
        male = a+b
    print(male, female+male)
