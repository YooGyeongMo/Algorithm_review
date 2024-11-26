N = int(input())

lst = list(map(int, input().split()))

lst.sort()

min_value = lst[0]
max_value = lst[N-1]

print(f"{min_value} {max_value}")

