import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1,T+1):
    text = input().strip()

    for i in range(1,11):
        if text[:i] == text[i:i*2]:
            print(f"#{test_case} {i}")
            break

