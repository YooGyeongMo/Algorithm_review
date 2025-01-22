def solution(food):
    answer = ''

    for i in range(1, len(food)):
        if food[i] // 2 == 0:
            continue
        answer += str(i) * (food[i] // 2)

    answer += '0' + answer[::-1]

    return answer


def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer


def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]