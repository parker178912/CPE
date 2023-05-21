def game(n, k):    
    wintime = {}
    losetime = {}
    for i in range(n):
        wintime[i+1] = 0
        losetime[i+1] = 0
    for i in range(int(k*n*(n-1)/2)):
        a, b, c, d = input().split()
        a = int(a)
        c = int(c)
        if b == "rock" and d == "scissors":
            wintime[a] = wintime[a]+1
            losetime[c] = losetime[c]+1
        elif b == "paper" and d == "rock":
            wintime[a] = wintime[a]+1
            losetime[c] = losetime[c]+1 
        elif b == "scissors" and d == "paper":
            wintime[a] = wintime[a]+1
            losetime[c] = losetime[c]+1        
        elif b == "scissors" and d == "rock":
            wintime[c] = wintime[c]+1
            losetime[a] = losetime[a]+1
        elif b == "paper" and d == "scissors":
            wintime[c] = wintime[c]+1
            losetime[a] = losetime[a]+1
        elif b == "rock" and d == "paper":
            wintime[c] = wintime[c]+1
            losetime[a] = losetime[a]+1
    for i in range(n):
        if int(wintime[i+1]+losetime[i+1])==0:
            print("-")
            continue
        print("%.3f"%(int(wintime[i+1])/(int(wintime[i+1]+losetime[i+1]))))
    print("")

while True:
    string = input() 
    if string == "0":
        break
    n, k = map(int, string.split())
    game(n, k)