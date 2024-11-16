# 0! 과 1! 은 1이다.

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i

    return result

print(factorial(5))

def recursive_factorial(i):
    if i <= 1:
        return 1
    return i * recursive_factorial(i-1)

print("재귀적으로 ", recursive_factorial(5))