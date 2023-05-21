while(True):
    try:
        x, y = map(int, input().split())
        m = x
        string = ''
        if x==1 or x==0 or y==1 or y==0 :
            print("Boring!")
            continue
        while(x>1):
            if x%y==0:
                x = int(x/y)
                string = string+' '+str(x)
            else:
                break
        if x==1:
            string = str(m)+string
            print(string)
        else:
            print("Boring!")
            continue
    except:
        break