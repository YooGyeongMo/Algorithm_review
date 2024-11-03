# n = int(input())
#
# data = list(map(int,input().split()))
#
# data.sort(reverse = True)
#
# print(data)
#
#
# n, m, k = map(int, input().split())
#
# print(n, m, k)

# 입력 수가 많을 시에 import sys sys.stdin.readline().rstrip() 사용

import sys
data = sys.stdin.readline().rstrip() #뒤에 개행을 엔터로 안받기 위해서 rstrip()사용  Hello World는 11개인데 rstrip()사용안하면 12개로 인식
print(data)

# print(len(data))
print(type(data))