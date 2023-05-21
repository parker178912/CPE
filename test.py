while True:
    a, b = map(int, input().split())
    time = a * b / 2
    dic = {}
    for i in range(time):
        player1, moves1, player2, moves2 = map(str, input().split())
        dic = {}
