for test_case in range(1,11):

    N = int(input())

    data_list = list(map(int, input().split()))

    result = 0

    for i in range(2,N-2):
        building = [
            data_list[i-2],
            data_list[i-1],
            data_list[i+1],
            data_list[i+2]
        ]

        max_value = max(building)

        if max_value < data_list[i]:
            result += data_list[i]- max_value

        # building =[]
        # max_value = 0
        # for j in range(i-2,i+3):


        #     if i == j:
        #         continue
        #     else:
        #         if max_value < data_list[j]:
        #             max_value = data_list[j]
        # if max_value < data_list[i]:
        #     result += data_list[i] - max_value

    print(f"#{test_case} {result}")