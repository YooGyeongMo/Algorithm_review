T = int(input())

for test_case in range(1, T+1):
    data_list= list(map(int, input().split()))

    max_value = max(data_list)
    min_value = min(data_list)

    data_list.remove(max_value)
    data_list.remove(min_value)

    result = sum(data_list) / 8

    print(f"#{test_case} {round(result,0)}") #가장가까운 정수 round 자릿수 실수 ,0