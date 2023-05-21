time = int(input())
for i in range(time):
    dic = {}
    M, Y, C, str = input().split()
    dic["M"] = int(M)
    dic["Y"] = int(Y)
    dic["C"] = int(C)
    for i in range(len(str)):
        if str[i]=="M":
            dic["M"] = dic["M"]-1
        elif str[i]=="C":
            dic["C"] = dic["C"]-1
        if str[i]=="Y":
            dic["Y"] = dic["Y"]-1
        if str[i]=="R":
            dic["M"] = dic["M"]-1
            dic["Y"] = dic["Y"]-1
        if str[i]=="B":
            dic["M"] = dic["M"]-1
            dic["Y"] = dic["Y"]-1
            dic["C"] = dic["C"]-1
        if str[i]=="G":
            dic["Y"] = dic["Y"]-1
            dic["C"] = dic["C"]-1
        if str[i]=="V":
            dic["M"] = dic["M"]-1
            dic["C"] = dic["C"]-1
    if dic["M"]<0 or dic["Y"]<0 or dic["C"]<0:
        print("NO")
    else:    
        print("YES", dic["M"], dic["Y"], dic["C"])
    