T = int(input())

for test_case in range(1, T + 1):
    A, B, N = map(int, input().split())

    count = 0

    while (A <= N and B <= N):
        if A < B:
            A += B
        else:
            B += A
        count+=1

    print(count)