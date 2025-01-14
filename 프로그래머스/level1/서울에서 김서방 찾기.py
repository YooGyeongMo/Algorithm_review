def solution(seoul):
    answer = seoul.index("Kim")

    return f"김서방은 {answer}에 있다"


arr = ["Jane", "Kim"]

print(solution(arr))


def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = i
            return f"김서방은 {answer}에 있다"


def findKim(seoul):
    # 함수를 완성하세요

    return "김서방은 {}에 있다".format(seoul.index('Kim'))