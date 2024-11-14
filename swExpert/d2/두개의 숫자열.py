T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    N_arr = list(map(int, input().split()))
    M_arr = list(map(int,input().split()))

    if N > M:
        N_arr, M_arr = M_arr, N_arr
        N, M = M, N

    max_value = 0

    for i in range(M-N+1):
        check_sum = 0
        for j in range(N):
            check_sum += N_arr[j] * M_arr[j+i]
        if max_value < check_sum:
            max_value = check_sum

    print(f"#{test_case} {max_value}")
