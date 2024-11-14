# 오 위 왼 밑
dx = [0, -1 ,0, 1]
dy = [1, 0, -1, 0]
dr = 0

N = int(input())

map_list = [[0]*N for i in range(N)]

data = list(map(str,input().split()))

x, y = 0, 0

for char in data:
    if char == 'R':
        dr = 0
        nx = x + dx[dr]
        ny = y + dy[dr]
        if 0 <= nx < N and 0 <= ny < N:
            map_list[x][y] = map_list[nx][ny]
            x, y = nx, ny

    if char == 'L':
        dr = 2
        nx = x + dx[dr]
        ny = y + dy[dr]
        if 0 <= nx < N and 0 <= ny < N:
            map_list[x][y] = map_list[nx][ny]
            x, y = nx, ny

    if char == 'U':
        dr = 1
        nx = x + dx[dr]
        ny = y + dy[dr]
        if 0 <= nx < N and 0 <= ny < N:
            map_list[x][y] = map_list[nx][ny]
            x, y = nx, ny

    if char == 'D':
        dr = 3
        nx = x + dx[dr]
        ny = y + dy[dr]
        if 0 <= nx < N and 0 <= ny < N:
            map_list[x][y] = map_list[nx][ny]
            x, y = nx, ny

print(f"{x+1} {y+1}")