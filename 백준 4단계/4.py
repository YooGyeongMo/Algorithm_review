import sys

data = []
# max_value = 0
# max_idx = 0

for i in range(9):
    data.append(int(input()))

# for i in range(9):
#     if max_value < data[i]:
#         max_value = data[i]
#         max_idx = i
#
# print(f"{max_value}\n{max_idx+1}")

max_value = max(data)
max_idx = data.index(max_value) + 1

print(f"{max_value}\n{max_idx}")