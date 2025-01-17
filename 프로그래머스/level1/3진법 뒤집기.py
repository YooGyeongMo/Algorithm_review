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