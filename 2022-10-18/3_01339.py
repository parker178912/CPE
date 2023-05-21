while(True):
    try:
        x = input()
        y = input()
        count1 = {}
        count2 = {}
        resol1 = []
        resol2 = []
        str1 = ""
        str2 = ""
        for i in x:
            count1[i] = count1.get(i, 0) +1
        for i, j in count1.items():
            resol1.append(str(j))
        for i in y:
            count2[i] = count2.get(i, 0) +1
        for i, j in count2.items():
            resol2.append(str(j))
        str1 = str1.join(sorted(resol1))
        str2 = str2.join(sorted(resol2))
        if str1 == str2:
            print("YES")
        else:
            print("NO")
    except:
        break
