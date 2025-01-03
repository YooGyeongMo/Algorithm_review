# N = int(input())
#
# for i in range(N):
#     print(" " * i + "*"* ((N*2-1)-(i*2)))
#
# for j in range(N-1,-1,-1):
#     print(" " * j-1)


N = int(input())

# 5입력
# 2*N 10에 9개 -> i 증가할때 9 개에서 몇개 빼야하나 9 7 5 3 1 순
for i in range(N):
    print(" " * i + "*" * ((2*N-1)-(i*2)) )

# 0까지 떨어져야함
for j in range(N-2,-1,-1):
    print(" " * j + "*" * ((2*N-1)-(j*2)) )
