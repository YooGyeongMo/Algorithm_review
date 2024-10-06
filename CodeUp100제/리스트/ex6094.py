n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

min_value = a[0]

for i in range(1,len(a)):
    if min_value > a[i]:
        min_value = a[i]

print(min_value)
