import sys

data_list = [0 for i in range(42)]

count = 0

for _ in range(10):
    data = int(sys.stdin.readline().rstrip())
    result = data % 42
    data_list[result] += 1

for num in data_list:
    if num >= 1:
        count += 1

print(count)