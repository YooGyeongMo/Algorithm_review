# N명의 사람들이 줄을 서 있다.
# 사람은 1번부터 N번까지 번호가 매겨져 있다.
# i번 사람이 돈을 인출하는데 걸리는 시간 Pi

# 5
# 3 1 4 3 2

N = int(input())

p_list = list(map(int,input().split()))

p_list.sort()

sum_1 = 0
sum_result = 0

for i in range(N):
    sum_1 += p_list[i]
    sum_result += sum_1

print(sum_result)


# 20분 걸림


# 다른 풀이

# N = int(input())
# P = list(map(int, input().split()))
#
# P.sort()
#
# answer = 0
# for i in range(1, N+1):
#     answer += sum(P[:i]) -> 리스트 인덱싱으로 풀기
#
# print(answer)