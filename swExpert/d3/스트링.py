import sys

sys.stdin = open("input.txt")

for _ in range(1,11):
    test_case = int(input())
    find = input()
    string_1 = input()
    result = 0
    # result = string_1.count(find)



    for i in range(len(string_1) - len(find) + 1):
        if find == string_1[i:i+len(find)]:
            result += 1

    print(f"#{test_case} {result}")
