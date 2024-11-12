T = int(input())

for test_case in range(1,T+1):
    day = int(input())
    day_list = list(map(int, input().split()))
    benefit = 0

    max_value = 0
    for i in range(day-1,-1,-1):
        if max_value < day_list[i]:
            max_value = day_list[i]
        else:
            benefit += max_value - day_list[i]
    print(f"#{test_case} {benefit}")
