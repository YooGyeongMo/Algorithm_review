# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()

def recursive_function2(i):
    if i == 100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    recursive_function2(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function2(1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= 1
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(5))

