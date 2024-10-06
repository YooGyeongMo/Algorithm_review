answer_list = []

for i in range(20):
    answer_list.append([])
    for j in range(20):
        answer_list[i].append(0)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    answer_list[a][b] = 1


for i in range(1,20):
    for j in range(1,20):
        print(answer_list[i][j], end =' ')
    print()