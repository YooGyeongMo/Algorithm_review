def solution(x, n):
    answer = []
    answer.append(x)
    for i in range(1,n):
        answer.append(answer[i-1] + x)
    return answer

print(solution(2,5))


def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

# 다른 풀이