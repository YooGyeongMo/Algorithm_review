# N = int(input())
#
# data = list(map(int,input().split()))
#
# C = int(input())
# # count = 0
#
# # for num in data:
# #     if C == num:
# #         count+=1
#
# print(data.count(C))

import sys
N = int(input())

result_list = list(map(int, sys.stdin.readline().split()))

C = int(input())

# count = 0
#
# for num in result_list:
#     if num == C:
#         count+=1

print(result_list.count(C))

