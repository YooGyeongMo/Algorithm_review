for test_case in range(1,11):
    N = int(input())

    data_list = [input() for i in range(8)]

    ans = 0

    #가로
    for i in range(8):
        for j in range(8-N+1):
            A = data_list[i][j:j+N]
            if A == A[::-1]:
                ans += 1

    #세로

    for i in range(8-N+1):
        for j in range(8):
            B =''
            for z in range(N):
                B += data_list[i+z][j]
            if B == B[::-1]:
                ans += 1

    print(f"#{test_case} {ans}")