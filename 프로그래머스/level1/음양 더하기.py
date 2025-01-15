def solution(absolutes, signs):
    answer = [i for i in absolutes]

    for i in range(len(signs)):
        if not signs[i]:
            answer[i] *= -1

    return sum(answer)



def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer



# absolutes = [4, 7, 12]
# signs = [True, False, True]
#
# zip(absolutes, signs) → [(4, True), (7, False), (12, True)]
# 
# for 루프에서의 작동
# • for absolute, sign in zip(absolutes, signs):는 **튜플을 언패킹(unpacking)**하여 absolute와 sign에 각각 저장합니다.