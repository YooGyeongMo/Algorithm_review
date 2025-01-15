def solution(left, right):
    a_list = [i for i in range(left, right + 1)]
    b_list = []
    answer = 0
    for i in a_list:
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        b_list.append(cnt)

    for x, y in zip(a_list, b_list):
        if y % 2 == 0:
            answer += x
        else:
            answer -= x

    return answer

# • 완전제곱수라면 약수 개수는 홀수.
# • 완전제곱수가 아니라면 약수 개수는 짝수.
# 완전 제곱수는 n = x^2 로 나타낼 수 있는 n

# 15는 완전 제곱수 아님 - 짝수
# print(15**0.5) - 3.872983346207417
# print(int(15**)) - 3

# 25 - 홀수 완전 제곱수
# 제곱근 정수 5 == 실수형 5.0 같음

