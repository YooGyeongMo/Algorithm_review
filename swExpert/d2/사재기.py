T = int(input())

for test_case in range(1,T+1):
    day = int(input())
    prices = list(map(int, input().split()))

    day_list = [0]*day
    max_price = 0
    benefit = 0
    for i in range(day-1,-1,-1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            benefit += max_price - prices[i]
    print(f"#{test_case} {benefit}")