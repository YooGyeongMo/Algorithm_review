# 19x19 배열 입력 받기 (1-based 인덱스를 사용)
d = [list(map(int, input().split())) for _ in range(19)]

n = int(input())  # 뒤집을 횟수 입력

for i in range(n):
    x, y = input().split()  # 좌표 입력 받기 (1-based)
    x = int(x)
    y = int(y)

    # 세로 방향 뒤집기 (열 고정, 각 행 값 바꿈)
    for j in range(1, 20):  # 1 ~ 19까지 반복
        if d[j - 1][y - 1] == 0:  # 1-based 좌표를 0-based 인덱스로 변환
            d[j - 1][y - 1] = 1
        else:
            d[j - 1][y - 1] = 0

    # 가로 방향 뒤집기 (행 고정, 각 열 값 바꿈)
    for j in range(1, 20):  # 1 ~ 19까지 반복
        if d[x - 1][j - 1] == 0:  # 1-based 좌표를 0-based 인덱스로 변환
            d[x - 1][j - 1] = 1
        else:
            d[x - 1][j - 1] = 0

# 결과 출력
for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")
    print()