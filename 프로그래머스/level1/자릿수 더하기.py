def solution(n):
    toStr = str(n)
    answer = 0

    for i in toStr:
        answer += int(i)

    return answer


def solution2(n):
    if n < 10:
        return n

    return n % 10 + solution(n // 10)

print(solution2(987))