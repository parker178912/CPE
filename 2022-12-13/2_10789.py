def count_primes(s):
    # create a dictionary to store the character frequency
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # find the prime numbers among the frequencies
    primes = ""
    for char, freq in freq_dict.items():
        # check if freq is a prime number
        is_prime = True
        if freq < 2:
            is_prime = False
        for i in range(2, int(freq**0.5) + 1):
            if freq % i == 0:
                is_prime = False
                break
        if is_prime:
            primes = primes + char
    if len(primes) != 0:
        return ''.join(sorted(primes))
    else:
        return "empty"

time = int(input())
for i in range(time):
    s = input()
    print("Case %d: "% (i+1), end = "")
    print(count_primes(s))
    