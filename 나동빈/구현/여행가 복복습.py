N = int(input())

a_list = list(map(str, input().split()))

# 왼 오 위 밑
nx = [0, 0, -1, 1]
ny = [-1, 1, 0, 0]

x, y = 1, 1

# 명령어 매핑
directions = {'L': 0, 'R': 1, 'U': 2, 'D': 3}

for i in a_list:
    if i in directions:
        d = directions[i]
        temp_x = x + nx[d]
        temp_y = y + ny[d]

    if 1<=temp_x <= N and 1<= temp_y <= N:
        x = temp_x
        y = temp_y

print(x,y)





move_types = ['L', 'R', 'U', 'D']


for i in a_list:
    for j in range(len(move_types)):
        if i == move_types[j]:
            tx = x + nx[j]
            ty = y + ny[j]
        if tx < 1 or tx > N or ty < 1 or ty > N:
            continue
        x, y = tx, ty

print(x,y)