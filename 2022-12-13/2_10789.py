def isPrime(num):
    if num == 1:
        return False
    max = num // 2
    for i in range(2, max + 1):
        if num % i == 0:
            return False
    return True


times = int(input())
for i in range(times):
    l = input()
    dic = {}
    for char in l:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    ans = ""
    for char in dic:
        num = dic[char]
        if isPrime(num) == True:
            ans += char
    if ans == "":
        print(f"Case {i+1}: empty")
    else:
        text = "".join(sorted(ans))  # ASCII
        print(f"Case {i+1}: {text}")
