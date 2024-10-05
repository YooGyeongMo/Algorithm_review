a,b,c = map(int, input().split())

result = a

for i in range(1,c):
    result += b

print(result)

# result = a + (n - 1) * d