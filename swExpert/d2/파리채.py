T = int(input())

for test_case in range(1,T+1):

    N, M = map(int,input().split())

    data_list = []

    for _ in range(N):
        data_list.append(list(map(int,input().split())))

    max_value = 0

    for i in range(N-M+1): #시작 범위
        for j in range(N-M+1): # 시작 범위
            flies = 0
            for si in range(i,i+M):
                for sj in range(j,j+M):
                    flies += data_list[si][sj]
            if max_value < flies: # max_value = max(max_value, flies)
                max_value = flies

    print(f"#{test_case} {max_value}")

