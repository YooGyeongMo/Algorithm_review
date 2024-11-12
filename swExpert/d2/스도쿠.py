import sys

sys.stdin = open('input.txt')

# 중복문제 set을 사용. set의 길이가 9개가 아니면 0을 리턴하면됨.

T = int(input())

def solve(data_list):
    #행검사
    for row in data_list:
        if len(set(row)) != N:
            return 0

    arr = list(zip(*data_list)) # 열을 행으로 바꿔서
    for col in arr:
        if len(set(col)) != N:
            return 0

    for i in range(0,N,3):
        for j in range(0,N,3):
            lst = data_list[i][j:j+3] + data_list[i+1][j:j+3] + data_list[i+2][j:j+3]
            if len(set(lst)) != N:
                return 0

            # lst = set()
            # for x in range(3):
            #     for y in range(3):
            #         lst.add(data_list[x+i][y+j])
            # if len(lst) != N:
            #     return 0

    return 1



for test_case in range(1,T+1):
    N = 9

    sdoku = [list(map(int, input().split())) for i in range(N)]

    ans = solve(sdoku)

    print(f"#{test_case} {ans}")