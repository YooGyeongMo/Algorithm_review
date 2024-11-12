T = int(input())
for i in range(T):
    N = int(input())
    result_list = [0 for _ in range(101)]
    data = list(map(int, input().split()))
    # max_idx = 0
    max_value = 0
    for num in data:
        result_list[num] += 1
    max_value = max(result_list)
    result = max([idx for idx, value in enumerate(result_list) if max_value == value])
    # for i in range(101):
    #     if result_list[i] == max_value:
    #         max_idx = i

    print(f"#{N} {result}")

