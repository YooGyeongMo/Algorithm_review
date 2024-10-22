N = int(input())

a = list(map(int, input().split()))
b = len(a)

#
# a.sort()

# print(a)
for i in range(b):
    min_idx = i
    for j in range(i+1,b):
        if a[min_idx] > a[j]:
            min_idx = j
    a[min_idx],a[i] = a[i], a[min_idx]
print(a[N//2])


