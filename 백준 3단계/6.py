import sys

N = int(input())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split()) # strip(), lstrip(), rstrip()

    print(a+b)
