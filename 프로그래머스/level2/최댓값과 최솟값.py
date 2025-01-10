def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))


def solution(s):
    answer = s.split()
    value = []
    for i in answer:
        value.append(int(i))

    value.sort()

    return str(value[0]) + " " + str(value[-1])