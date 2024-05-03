# T = int(input())
# #테스트 케이스를 받는다.
#
# for i in range(1, T+1):
#     m = input().split()
#     sum = 0
#     mean = 0
#     for j in range(10):
#         num = int(m[j])
#         sum += num
#     mean = round(sum / 10)
#     print(f"#{i} {mean}")

T = int(input())

for i in range(1, T+1):
    m = list(map(int, input().split()))
    sum = 0
    mean = 0
    for j in range(10):
        num = m[j]
        sum += num
    mean = round(sum/10)
    print(f"#{i} {mean}")

