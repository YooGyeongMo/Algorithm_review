N = int(input())

data_list = [str(i) for i in range(1,N+1)]

result = []


for string in data_list:
    cnt = 0
    for char in string:
        if char in '369':
            cnt += 1

    if cnt > 0:
        result.append("-" * cnt)
    else:
        result.append(string)

print(f"{' '.join(map(str,result))}")
