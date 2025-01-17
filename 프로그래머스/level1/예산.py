def solution(d, budget):
    d.sort()
    cnt = 0
    total = 0
    for cost in d:
        if total + cost > budget:
            break
        total += cost
        cnt += 1

    return cnt


def solution(d, budget):
    d.sort()
    cnt = 0
    hab = 0

    for cost in d:
        hab += cost
        if hab > budget:
            break
        cnt += 1

    return cnt