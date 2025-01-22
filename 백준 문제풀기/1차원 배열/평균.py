import sys

N = int(input())

arr = list(map(int,sys.stdin.readline().split()))

a_list = []

max_value = max(arr)

for i in arr:
    target = (i/max_value) * 100
    a_list.append(target)

print(sum(a_list)/N)