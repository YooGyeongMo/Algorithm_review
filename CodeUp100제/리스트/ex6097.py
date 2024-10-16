h, w = map(int, input().split()) #세로(행), 가로(열)

a_list = [[0 for j in range(w)]for i in range(h)]

stick = int(input())

for _ in range(stick):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if d == 0: #행 고정 열을 ++
        for i in range(l):
            a_list[x][y+i] = 1
    else:
        for i in range(l):
            a_list[x+i][y] = 1

for i in range(h):
    for j in range(w):
        print(a_list[i][j], end = " ")
    print()