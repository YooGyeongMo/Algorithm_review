# 오름 차순으로 동전 종류가 주어짐
# 배열로 받아서 스택으로 pop해서 배열이 빌때까지 while 돌고 비면 마지막 최소값하면됨
# 먼저 필요한 동전 갯수 result
# K원을 나누고 떨어지고 저장을 해야함.
# 그게 큰수로 최대로 떨어질수 있을때 까지 이걸 갯수로 해야함


N, K = map(int, input().split())

coin_type = []

coin_count = 0

for i in range(N):
    coin = int(input())
    coin_type.append(coin)

# coin_type.sort(reverse = True)

while K > 0:
    coin_max = coin_type.pop()

    if coin_max <= K:
        coin_count += K // coin_max
        K %= coin_max

# for i in coin_type:
#     coin_count += K // i
#     K %= i


print(coin_count)