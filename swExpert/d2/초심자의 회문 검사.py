T = int(input())

for test_case in range(1,T+1):
    N = input().strip()

    reverse_word = N[::-1]

    print(f"#{test_case} {1 if N == reverse_word else 0}")

    # for i in range(len(N)-1, -1, -1):
    #     result += N[i]
    #
    # if result == N:
    #     print(f"#{test_case} 1")
    # else:
    #     print(f"#{test_case} 0")

