import sys
sys.stdin = open("input.txt")

for test_case in range(1,11):
    N = int(input())

    data_list = [input() for j in range(8)]

    ans = 0

    for x in range(8):
        for y in range(8-N+1):
            A = data_list[x][y:y+N]
            if A == A[::-1]:
                ans += 1

    #세로
    for x in range(8-N+1):
        for y in range(8):
            B = ''
            for z in range(N):
                B += data_list[x+z][y]
            if B == B[::-1]:
                ans+=1

    print(f"#{test_case} {ans}")