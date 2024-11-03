# T = int(input())
# test_num = int(input())
#
#
# for _ in range(T):
#     a_list = {x: 0 for x in range(0, 101)}
#     b = list(map(int,input().split()))
#     for num in b:
#         if num in a_list:
#             a_list[num] += 1
#
#     max_value = max(a_list.values())
#     result = max([key for key, value in a_list.items() if max_value == value])
#
#
#     print(f"#{test_num} {result}")


T = int(input())

for _ in range(T):
    test_num = int(input())
    a_list = [0] * 101
    b_list = list(map(int,input().split()))
    for num in b_list:
        a_list[num] += 1
    max_value = max(a_list)
    result = max([idx for idx, value in enumerate(a_list) if value == max_value])

    print(f"#{test_num} {result}")