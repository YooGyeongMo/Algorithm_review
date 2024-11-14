T = int(input())

for test_case in range(1,T+1):

    N = int(input())
    primes = [2, 3, 5, 7, 11]
    exponent = []

    for prime in primes:
        count = 0
        while N % prime == 0:
            N //= prime
            count += 1

        exponent.append(count)

    print(exponent)