T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    N_str = list(str(N))
    N_len = len(N_str)
    max_value = 0
    count = 0
    while count < M:
        for i in range(N_len-1,-1,-1):
            if N_str[i] < N_str[N_len-i]:
                N_str[N_len-i],N_str[i] = N_str[i],N_str[N_len-i]
                count += 1

    print(f"{test_case} {N_str}")