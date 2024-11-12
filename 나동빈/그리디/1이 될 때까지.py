# N, K = map(int,input().split())
#
# count = 0
#
# while N != 1:
#     if N % K == 0:
#         N = N // K
#         count += 1
#         continue
#     N -= 1
#     count += 1
#
# print(count)

n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)
