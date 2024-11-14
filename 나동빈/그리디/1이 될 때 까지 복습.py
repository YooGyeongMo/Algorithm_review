N , K = map(int, input().split())

namuji = N%K

count = namuji

while True:
    if N == 1:
        break

    N //= K
    count += 1

print(count)
