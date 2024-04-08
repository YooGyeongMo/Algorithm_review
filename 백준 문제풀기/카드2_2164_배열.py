N = int(input())
# arr = [*range(1,N +1)]

arr = []
for i in range(1, N+1):
    arr.append(i)
# print(arr)
while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))
    # print(arr)

print(arr.pop())

#  배열은 시간 초과
# list를 쓴 코드는 시간초과