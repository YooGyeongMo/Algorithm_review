N, M = map(int, input().split())

blanket = [i for i in range(1,N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = blanket[i-1:j]
    tmp.reverse()
    blanket[i-1:j] = tmp

for num in blanket:
    print(num, end= " ")