import sys

N, X = map(int,input().split())

data_list = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    if data_list[i] < X:
        print(f"{data_list[i]}",end=" ")