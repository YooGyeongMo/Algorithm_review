import sys

a, b = map(int, input().split())
print(a-b)

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(str(a-b))