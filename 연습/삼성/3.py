for test_case in range(1,11):
    dump = int(input())

    data_list = list(map(int, input().split()))

    result = 0

    for i in range(dump):

        max_value = max(data_list)
        max_idx = data_list.index(max_value)

        min_value = min(data_list)
        min_idx = data_list.index(min_value)

        data_list[max_idx] -= 1
        data_list[min_idx] += 1

        if max(data_list) - min(data_list) <= 1:
            break

    result = max(data_list) - min(data_list)

    print(f"#{test_case} {result}")