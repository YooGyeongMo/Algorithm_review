miro_list = [list(map(int, input().split())) for _ in range(10)]

x, y = 1, 1

for i in range(1,10):
    for j in range(1,10):

        if miro_list[x][y] == 2:
            miro_list[x][y] = 9
            break

        miro_list[x][y] = 9

        if miro_list[x][y+1] != 1:
            y += 1
        elif miro_list[x+1][y] != 1:
            x += 1
        else:
            break
    if miro_list[x][y] == 9:
        break

def print_arr():
    for i in range(10):
        for j in range(10):
            print(miro_list[i][j],end=" ")
        print()

print_arr()