import sys

N = int(input())

result = 0

data_list = list(map(int, sys.stdin.readline().split()))


for num in data_list:
    aver = (num/max(data_list)) * max(data_list)
    result += aver

dap = result/N

print(dap)