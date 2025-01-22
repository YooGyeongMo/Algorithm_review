def solution(array, commands):
    answer = []
    for i in commands:
        answer.append((sorted(array[i[0] - 1: i[1]]))[i[2] - 1])

    return answer


def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer


def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1:j])[k - 1])

    return answer


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1: x[1]])[x[2] - 1], commands))