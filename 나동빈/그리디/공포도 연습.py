N = int(input())

a_list = list(map(int,input().split()))

a_list.sort()

result = 0
group_count = 0

for i in a_list:
    group_count += 1
    if group_count >= i:
        result += 1
        group_count = 0

print(result)