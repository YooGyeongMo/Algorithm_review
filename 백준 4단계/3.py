import sys

N = int(input())

data_list = list(map(int,sys.stdin.readline().split()))

# data_list.sort()
# max_value = data_list[N-1]
# min_value = data_list[0]
#
# print(f"{min_value} {max_value}")

print(f"{min(data_list)} {max(data_list)}")