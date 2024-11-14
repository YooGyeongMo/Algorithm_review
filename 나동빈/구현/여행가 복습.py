n = int(input())

# 왼 위 오 밑
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
plan_type = ['L', 'U', 'R', 'D']

x, y = 1, 1

plans = input().split()

for plan in plans:

    # for i in range(len(plan_type)):
    idx = plan_type.index(plan)

    nx = x + dx[idx]
    ny = y + dy[idx]

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x, y)
