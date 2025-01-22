import sys

T = int(input())

for test_case in range(1,T+1):
    N = sys.stdin.readline().rstrip()

    N = N[0] + N[-1]

    print(N)