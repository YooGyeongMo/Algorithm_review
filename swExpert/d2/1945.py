T = int(input())

# for test_case in range(1,T+1):
#     N = int(input())
#     a = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
#     for num in a.keys():
#         while N%num==0:
#             a[num] +=1
#             N //= num
#     print(f"#{test_case} {a[2]} {a[3]} {a[5]} {a[7]} {a[11]}")

for test_case in range(1, T + 1):
    N = int(input())

    a = 0
    while (N % 2 == 0):
        a += 1
        N //= 2
    b = 0
    while (N % 3 == 0):
        b += 1
        N //= 3
    c = 0
    while (N % 5 == 0):
        c += 1
        N //= 5
    d = 0
    while (N % 7 == 0):
        d += 1
        N //= 7
    e = 0
    while (N % 11 == 0):
        e += 1
        N //= 11

    print(f"#{test_case} {a} {b} {c} {d} {e}")
