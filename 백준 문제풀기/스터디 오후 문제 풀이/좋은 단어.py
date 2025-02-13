import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    word = input().rstrip()

    if not word:
        continue

    stack = []
    for i in range(len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])
    if not stack:
        cnt += 1

print(cnt)