import sys

a, b = map(float, input().split())
print(a/b)

a, b = map(float, sys.stdin.readline().split())
sys.stdout.write(str(a/b))