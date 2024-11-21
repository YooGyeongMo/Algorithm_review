for _ in range(1,T+1):
    test_case = int(input())

    data_list =[list(map(int,input().split())) for j in range(100)]


    dae_1 = 0
    dae_2 = 0
    result = 0
    for i in range(100):
        row = 0
        col = 0
        result = max()
        for j in range(100):
            row += data_list[i][j]
            col += data_list[j][i]
        dae_1 += data_list[i][i]
        dae_2 += data_list[i][99-j]



