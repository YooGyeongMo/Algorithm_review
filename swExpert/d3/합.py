import sys
sys.stdin = open("input.txt")

for _ in range(10):
    test_case = int(input())

    data_list = [list(map(int,input().split())) for _ in range(100)]

    col_sum = 0
    row_sum = 0
    dae_1 = 0
    dae_2 = 0
    # max_value = []
    ans = 0
    for i in range(100): # 0 ~ 99

        col_sum = row_sum = 0

        for j in range(100):
            row_sum += data_list[i][j]
            col_sum += data_list[j][i]

        ans = max(ans, row_sum, col_sum)


        dae_1 += data_list[i][i]
        dae_2 += data_list[i][99-i]

    ans = max(ans, dae_1, dae_2)




    print(f"#{test_case} {ans}")
