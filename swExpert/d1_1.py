# j = int(input())
#
# for i in range(j):
#     sum = 0
#     nums = input().split()
#     for num_str in nums:
#         num = int(num_str)
#         print(num_str)
#         if num % 2 != 0:
#             sum += num
#     print(f"#{i+1} {sum}")

T = int(input())
# 여러개의 테스트 케이스를 얼마나 테스트할지 T에 담는다.

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    #10개의 숫자를 받는다.
    sum = 0
    for i in range(10):
        if num[i] % 2 == 1:
            sum += num[i]
    print(f"#{test_case} {sum}")
