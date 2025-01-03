# 방법 1

# N = int(input())
#
# for i in range(1, N * 2):
#     if i > N:
#         print("*" * (N - (i - N)) + " " * ((N * 2) - (2*(N - (i - N)))) + "*" * (N - (i - N)))
#     else:
#         print("*" * i + " " * ((N * 2) - (i * 2)) + "*" * i)

# 방법 2

N = int(input())


for i in range(1,N+1):
    print("*"*i + " " * 2*(N-i) + "*"*i)
for i in range(N-1,0,-1):
    print("*"*i + " " * 2*(N-i) + "*"*i)