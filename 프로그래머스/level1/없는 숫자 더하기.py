def solution(numbers):
    answer = 0
    a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in numbers:
        if i in a_list:
            a_list.remove(i)

    answer = sum(a_list)

    return answer



def solution(numbers):
    return 45 - sum(numbers)


solution = lambda x: sum(range(10)) - sum(x)


def solution(numbers):
    answer=0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer