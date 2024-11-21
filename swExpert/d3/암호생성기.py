for _ in range(10):
    test_case = int(input())

    data_list = list(map(int,input().split()))


    while True:
        for i in range(1,6):
            first = data_list.pop(0) - i

            if first == 0 or first < 0:
                first = 0
                data_list.append(first)
                break

            data_list.append(first)

        if data_list[-1] == 0:
            break

    print(f"#{test_case} {' '.join(map(str, data_list))} ")

