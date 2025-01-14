def solution(n):
    answer = list(map(int, str(n)))

    answer.sort(reverse=True)

    return int(''.join(map(str,answer)))

print(solution(83929))