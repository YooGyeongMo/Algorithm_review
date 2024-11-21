T = int(input())

for test_case in range(1,T+1):

    data_list = list(map(int,input().split()))

    sum_list = sum(data_list)

    result = round(sum_list/10)

    print(result)