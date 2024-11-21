T = int(input())

for test_case in range(1,T+1):

    N = int(input())

    data_list = list(map(int,input().split()))

    max_value = 0

    result = 0

    for i in range(N-1,-1,-1):
        if max_value < data_list[i]:
            max_value = data_list[i]
        else:
            result += max_value - data_list[i]

    print(f"{test_case} {result}")
