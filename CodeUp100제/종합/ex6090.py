start, mul, add, order = map(int, input().split())

result = start

for i in range(1,order):
    result *= mul
    result += add

print(result)