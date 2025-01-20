def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer_set = set(answer)
    answer_set = list(answer_set)
    answer_set.sort()

    return answer_set

# set 중복허용하지 않는다. 순서가 없다 그래서 리스트로 변환하고 소팅 O(1) 복잡도 가짐
# .add .remove 로 추가한다.

# 사용 사례
# 	•	데이터의 중복 제거.
# 	•	값의 존재 여부 확인 (in 연산자 사용).
# 	•	수학적 집합 연산(교집합, 합집합 등).


# 2. dictionary (사전)
#
# 특징
# 	•	**키-값 쌍(key-value pairs)**으로 데이터를 저장.
# 	•	키는 중복을 허용하지 않음, 하지만 값은 중복 가능.
# 	•	순서 유지: Python 3.7부터 삽입된 순서를 유지.
# 	•	가변적: 값을 추가/삭제할 수 있음.
#
# 사용 사례
# 	•	키-값 형태로 데이터를 저장하고 빠르게 검색할 때.
# 	•	값 대신 키를 사용해 데이터를 조회 가능 (O(1) 평균 시간 복잡도).