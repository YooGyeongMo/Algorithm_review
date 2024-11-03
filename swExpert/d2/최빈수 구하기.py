T = int(input())


for test_case in range(1, T+1):
    b = int(input())
    a = list(map(int, input().split()))
    score_list = [0] * 101

    for num in a:
        score_list[num] += 1

    max_score = score_list[0]
    max_idx = 0
    for i in range(1,len(score_list)):
        if score_list[i] > max_score:
            max_score = score_list[i]
            max_idx = i
        elif score_list[i] == max_score and i > max_idx:
            max_idx = i

    print(f"#{b} {max_idx}")