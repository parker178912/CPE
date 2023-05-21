x = int(input())
for i in range(1,x+1):
    input()
    date1 = input()
    date2 = input()
    nowday, nowmonth, nowyear = map(int, date1.split('/'))
    bornday, bornmonth, bornyear = map(int, date2.split('/'))
    if bornyear>nowyear or (bornyear == nowyear and bornmonth > nowmonth) or ( bornyear == nowyear and bornmonth == nowmonth and bornday>nowday):
        print("Case #%d: Invalid birth date"%i)
        continue    
    else:
        if nowyear-bornyear>131:
            print("Case #%d: Check birth date"%i)
        elif nowmonth>bornmonth or (nowmonth==bornmonth and nowday>=bornday):
            print("Case #%d:"%i,nowyear-bornyear)
        else:
            print("Case #%d:"%i,nowyear-bornyear-1)
