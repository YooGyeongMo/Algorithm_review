a = [list(map(int, input().split()))for _ in range(19)]

# for i in range(19):
#     a.append([])
#     for j in range(19):
#         a[i].append(0)

# 19x19 배열을 미리 0으로 초기화
# for i in range(19):
#     a.append([0] * 19)

# a = [[0 for j in range(19)]for i in range(19)]

# for i in range(19):
#     a[i] = list(map(int, input().split()))



num = int(input())

for i in range(num):
    b, c = map(int, input().split())
    for j in range(1,20):
        if(a[j-1][c-1] == 1 ):
            a[j-1][c-1] = 0
        elif(a[j-1][c-1] == 0 ):
            a[j-1][c-1] = 1
        if(a[b-1][j-1] == 1):
            a[b-1][j-1] = 0
        elif(a[b-1][j-1] == 0):
            a[b-1][j-1] = 1

for i in range(19):
    for j in range(19):
        print(a[i][j], end = " ")
    print()
