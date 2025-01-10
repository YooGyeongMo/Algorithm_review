def solution(num):
    if num % 2 == 0 or num == 0 :
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer


def solution2(num):
    if num % 2:
        return 'Odd'

    return 'Even'