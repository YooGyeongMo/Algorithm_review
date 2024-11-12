# import sys
#
# data_list = []
# result_list = []
#
# for _ in range(28):
#     data_list.append(int(sys.stdin.readline().rstrip()))
#
#
# for i in range(1,31):
#     if i not in data_list:
#         result_list.append(i)
#
# result_min = min(result_list)
# result_max = max(result_list)
#
# print(f"{result_min}\n{result_max}")
#


import sys

data_list = [i for i in range(1,31)]

for _ in range(28):
    data = (int(sys.stdin.readline().rstrip()))
    data_list.remove(data)

print(min(data_list))
print(max(data_list))