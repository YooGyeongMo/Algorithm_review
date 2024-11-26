N = int(input())

result = sum([i for i in range(1,N+1)])

print(result)

# sum = 0
#
# for i in range(1,N+1):
#     sum += i
#
# print(sum)

#
# def recursive(N):
#     if N == 0:
#         return 0
#     return N + recursive(N-1)

# 3 + recursive(2) 3+3
# 2 + recursive(1) 3
# 1 + recursive(0) 0 1
# print(recursive(N))
