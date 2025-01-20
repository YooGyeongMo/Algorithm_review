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


# 회의실, 공포도와 같은 문제처럼 그리디에서 주는 조건을 잘보자
# 해당 조건에서 최대한 많은 것을 뽑으려하면 정렬하고 백트래킹을 하거나, 앞에서부터 작은 값을 채워가면 최대 그룹을 만들 수 있다.