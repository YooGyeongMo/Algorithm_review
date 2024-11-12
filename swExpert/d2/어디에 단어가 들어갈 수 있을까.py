import sys

sys.stdin = open("input.txt")

def arr_count(data_arr):

    result = 0

    for lst in data_arr:
        cnt = 0
        for i in range(len(lst)):
            if lst[i]:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
    return result

T = int(input())

for test_case in range(1,T+1):

    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(N)] +  [[0]*(N+1)]
    arr_trans = list(map(list, zip(*arr)))

    ans = arr_count(arr) + arr_count(arr_trans)

    print(f"#{test_case} {ans}")