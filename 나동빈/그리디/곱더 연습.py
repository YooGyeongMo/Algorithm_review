import sys
# readline() 함수만 사용하면 입력 예시: "10 20\n"

S = sys.stdin.readline().rstrip()

# if len(S) == 1:
#     print(int(S))
#
# result = 0
#
# for i in range(len(S)):
#     if int(S[i]) == 0 or int(S[i]) == 1:
#         result += int(S[i])
#     else:
#         if result == 0:
#             result += int(S[i])
#         else:
#             result *= int(S[i])
#
# print(result)


result = int(S[0])

for i in range(1,len(S)):
    num = int(S[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)