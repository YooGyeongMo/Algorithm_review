T = int(input())

for _ in range(T):

    test_num = int(input())

    score_list = [0] * 101

    student_list = list(map(int,input().split()))

    for num in student_list:
        score_list[num] += 1

    max_value = max(score_list)
    # max_idx = 0

    max_idx = max([idx for idx, value in enumerate(score_list) if max_value == value])

    # for i in range(101):
    #     if max_value == score_list[i]:
    #         max_idx = i

    print(f"#{test_num} {max_idx}")