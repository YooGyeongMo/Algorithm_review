N, M = map(int,input().split())
ball_num = [0] * N

for _ in range(M):
    i, j, k = map(int,input().split())
    ball_num[i-1:j] = [k] * (j-i+1)
    # for x in range(i-1,j):
    #     ball_num[x] = k

for i in range(len(ball_num)):
    print(ball_num[i], end=" ")

    # # 슬라이스 범위에 값을 설정하기 위해 [k] * (j - i + 1) 사용
    # ball_num[i - 1:j] = [k] * (j - i + 1)