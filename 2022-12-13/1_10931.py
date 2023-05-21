while True:
    num = int(input())
    if num == 0:
        break
    count = 0
    l = ""
    while num > 0:
        temp = num % 2  # remainder
        l = str(temp) + l
        if temp == 1:
            count += 1
        num = num // 2
    print(f"The parity of {l} is {count} (mod 2).")
