T = int(input())

for _ in range(T):
    test_case = int(input())

    data_list = list(map(int, input().split()))

    scores = [0] * 101

    for num in data_list:
        scores[num] += 1

    max_value = max(scores)

    result = max([idx for idx,value in enumerate(scores) if max_value == value])

    print(f"#{test_case} {result}")