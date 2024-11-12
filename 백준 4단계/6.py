N, M = map(int, input().split())

ball_num = [i for i in range(1,N+1)]

for _ in range(M):
    i, j = map(int,input().split())

    ball_num[i-1], ball_num[j-1] = ball_num[j-1], ball_num[i-1]

for num in ball_num:
    print(num,end=" ")