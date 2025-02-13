def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

# hashDict = {}
# hashDict[hash("Alice")] = "Alice"
#
# print(hashDict[hash("Alice")])  # "Alice" 출력


def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for person in participant:
        hashDict[hash(person)] = person #해시 값을 키값으로 정하고 해당 문자열을 value로 저장
        sumHash += hash(person) # 모든 해시 값을 더해서 저장

    for i in completion:
        sumHash -= hash(i) # 해시값을 빼다보면 남는게 완주 못한사람.

    return hashDict[sumHash]


def soultion(participant, completion):

    from collections import Counter

    answer = Counter(participant) - Counter(completion)

    return list(answer.key())[0]

# list(answer.keys()) 남은 Counter객체 (딕셔너리 형태로 저장된 answer )에
#
# 키값들만 뽑아오는데 그건 딕셔너리가 아니라 하나의 value값이니까 그걸 list화 시켜서 그중에 0번째를 들고오는거