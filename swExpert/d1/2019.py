N = int(input())

answer = 0

for i in range(0,N+1):
    answer = 1<<i
    print(answer,end = " ")