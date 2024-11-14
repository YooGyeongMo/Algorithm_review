day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for test_case in range(1, T+1):

    M_1, D_1, M_2, D_2 = map(int, input().split())

    result = 0

    if M_1 == M_2:
        result = D_2 - D_1 +1

    else:
        result = day[M_1-1] - D_1 + 1

        for i in range(M_1, M_2-1):
            result += day[i]

        result += D_2

    # elif M_1 < M_2:
    #     for i in range(M_1-1, M_2):
    #
    #         if i == M_1-1:
    #             result = day[M_1-1] - D_1 +1
    #         elif i == M_2-1:
    #             result += D_2
    #         else:
    #             result += day[i]

    print(f"#{test_case} {result}")