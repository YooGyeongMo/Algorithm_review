T = int(input())

for test_case in range(1,T+1):
    data = list(map(int, input().split()))

    group = 0
    count = 0

    for i in data:
        count += 1

        if i <= count:
            group += 1
            count = 0


    print(f"#{test_case} {group}")