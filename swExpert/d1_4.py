T = int(input())

for test_case in range(1,T+1):
    m = list(map(int, input().split()))
    max = 0
    for i in range(10):
        num = m[i]
        if max < m[i]:
            max = m[i]
    print(f"#{test_case} {max}")