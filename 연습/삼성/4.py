for _ in range(10):
    test_case = int(input())

    find = input().strip()

    string_1 = input().strip()

    # print(f"#{test_case} {string_1.count(find)}")

    count = 0

    for i in range(len(string_1)-len(find)+1):

        if find == string_1[i:i+2]:
            count += 1

    print(f"#{test_case} {count}")
