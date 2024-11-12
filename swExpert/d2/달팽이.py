T = int(input())

# 오 밑 왼 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())
    data_list = [[0 for j in range(N)] for i in range(N)]

    x, y = 0, 0
    cnt = 1
    dr = 0

    for _ in range(N * N):
        data_list[x][y] = cnt
        cnt += 1
        nx = x + dx[dr]
        ny = y + dy[dr]

        if 0 <= nx < N and 0 <= ny < N and data_list[nx][ny] == 0:
            x, y = nx, ny
        else:
            dr = (dr + 1) % 4
            x, y = x + dx[dr], y + dy[dr]

    print(f"#{test_case}")
    # for row in data_list:
    #     # print(*row)
    #     print(" ".join(map(str, row)))
    #
    for i in range(N):
        for j in range(N):
            print(data_list[i][j], end = " ")
        print()