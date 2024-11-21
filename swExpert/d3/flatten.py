import sys

sys.stdin = open("input.txt")

for test_case in range(1,11):

    dump = int(input())

    data_list = list(map(int, input().split()))

    for i in range(dump):
        data_list.sort()

        data_list[0] += 1
        data_list[-1] -= 1


        if max(data_list) - min(data_list) <= 1:
            break

    result = max(data_list) - min(data_list)
    print(f"#{test_case} {result}")








