def solution(a, b):
    answer = 0

    for x, y in zip(a, b):
        answer += x * y
    return answer

# enumerate(iterable, start=0)
#
# enumerate 반환 값
# • 반복 시 (index, value) 형태의 튜플을 반환합니다.