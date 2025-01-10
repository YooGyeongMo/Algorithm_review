def solution(s):
    answer = int(s)

    return answer

print(solution("-441"))

def solution2(s):
    answer = 0
    for idx, value in enumerate(s[::-1]):
        if value == '-':
            answer *= -1
        else:
            answer += int(value) * (10 ** idx)
    return answer

print(solution2("-5526"))