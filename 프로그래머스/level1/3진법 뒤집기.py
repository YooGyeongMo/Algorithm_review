def solution(n):
    answer = 0

    if n == 0:
        return 0
    arr = []
    while n > 0:
        arr.append(n % 3)
        n //= 3

    arr = arr[::-1]
    for i in range(len(arr)):
        answer += arr[i]*(3 ** i)

    return answer




def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

# 구현처럼 그냥 간단하게 3진법일 때 0으로 나오면 바로 0이 떨어지게하고 다른 예외, 조건들을 처리하였다.
# //은 나머지 몫이 정수형까지만 되기에 /과는 차이가 있다. 무조건 다 떨어지게 계산하지 않는 점에서 진법 계산에 사용가능하다.
# answer = int(tmp, 3)  # 저장된 문자열을 3진법으로 해석해 10진수로 변환한다...
# int()는 두 번째 매개변수로 진법(base)을 받을 수 있다.
print(int("101", 2))    # 2진수 → 10진수: 5
print(int("1A", 16))    # 16진수 → 10진수: 26
print(int("77", 8))     # 8진수 → 10진수: 63
# 문자 기반의 숫자 변환
print(int('A', 16))  # 'A'는 16진수에서 10진수로 변환: 10
print(int('F', 16))  # 16진수 'F': 15