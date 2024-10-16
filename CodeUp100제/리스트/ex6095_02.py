pan = []

for i in range(20):
    pan.append([])
    for j in range(20):
        pan[i].append(0)  # i번째 줄에 다 0 대입

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    pan[a][b] = 1


for i in range(1,20):
    for j in range(1,20):
        print(pan[i][j],end=' ')
    print()
