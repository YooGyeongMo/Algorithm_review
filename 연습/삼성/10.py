T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    data_list = []
    for i in range(N):
        data_list.append(list(map(int,input().split())))

    max_value = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies = 0

            for x in range(i, i + M):
                for y in range(j, j + M):
                    flies += data_list[x][y]
            if max_value < flies:
                max_value = flies

    print(f"#{test_case} {max_value}")

