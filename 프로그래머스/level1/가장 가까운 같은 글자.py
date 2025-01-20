def solution(s):
    answer = [-1] * len(s)

    for i in range(len(s)):
        for j in range(i):
            if s[i] == s[j]:
                answer[i] = i - j

    return answer


# 키 - 값 in 은 키값으로
def solution(s):
    answer = []
    dic = {}

    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i-dic[s[i]]) # 현재까지 인덱스에서 dic[인덱스] 에 등장한것의 인덱스 거리
        dic[s[i]] = i # 현재의 인덱스를 저장한다.

    return answer