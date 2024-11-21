def recursive(x,y):
    if y == 1:
        return x

    return x * recursive(x, y-1)



for _ in range(1,11):
    test_case = int(input())

    N, M = map(int,input().split())

    result = recursive(N,M)

    print(f"#{test_case} {result}")