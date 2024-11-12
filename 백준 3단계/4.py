# 첫째 입력 -> 총가격
# 둘째 입력 -> 총 물건 종류
# 3번째 부터 -> 각 물건 가격과 갯수

X = int(input())

N = int(input())

all_price = 0

for _ in range(N):
    a, b = map(int, input().split())
    all_price += a * b

if X == all_price:
    print("Yes")
else:
    print("No")