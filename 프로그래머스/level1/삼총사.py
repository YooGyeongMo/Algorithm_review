def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for z in range(j+1, len(number)):
                if number[i] + number[j] + number[z] == 0:
                    answer += 1
    return answer


def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt


# 브루트포스로 모든 경우를 탐색했다. - 완전탐색 그러나 O^n3 이나옴.
# itertools의 존재를 알았지만 어떻게 사용하는지 몰랐다. 조합문제인걸 알았어도 구현으로 풀었었는데 조합 라이브러리는 알아두자.