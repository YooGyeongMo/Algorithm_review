n = int(input())
a = input().split()
answer = []

for i in range(n):
    a[i] = int(a[i])

for i in range(24):
    answer.append(0)

for i in range(n):
    answer[a[i]] += 1

for i in range(1,len(answer)):
    print(f"{answer[i]}", end =' ')