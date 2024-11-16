from collections import deque

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    # 큐가 빌때까지
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or N <= nx or 0 < ny or M <= ny:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]

N, M = map(int, input().split())

graph = [list(map(int, input())) for j in range(N)]


# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))

print(graph)