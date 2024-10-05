# a, b, c = map(int, input().split())
#
# result = a
#
# for i in range(1,c):
#     result += b
#
# print(result)
a, b, c = map(int, input().split())



result = a + (b*(c-1))

print(result)