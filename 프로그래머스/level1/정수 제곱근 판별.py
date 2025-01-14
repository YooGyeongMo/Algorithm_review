# def solution(n):
#     x = int(n ** 0.5)
#
#     if n == x ** 2:
#         return (x + 1) ** 2
#     else:
#         return -1

# n == x^2 인데
# 제곱근을 구할때는 import math 이후

# math.sqrt(n) 하거나 n 에 0.5 곱해주면 된다.


import math


def solution(n):
    x = math.sqrt(n)

    if n == x ** 2:
        return (x + 1) ** 2
    else:
        return -1

print(solution(121))