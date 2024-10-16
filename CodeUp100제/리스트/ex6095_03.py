d = [[0 for j in range(20)]for i in range(20)]

# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    d[a][b] = 1

def print_arr():
    for i in range(1,20):
        for j in range(1,20):
            print(d[i][j], end = " ")
        print()


print_arr()
