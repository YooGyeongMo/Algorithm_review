def solution(n):
    answer = ''

    if n % 2 == 0:
        while n != 0:
            if n % 2 == 0:
                answer += '수'
            else:
                answer += '박'
            n -= 1
    else:
        for i in range(n):
            if i % 2 == 0:
                answer += '수'
            else:
                answer += '박'

    return answer



def solution(n):
    answer = ("수박"*n)[:n]
    return answer