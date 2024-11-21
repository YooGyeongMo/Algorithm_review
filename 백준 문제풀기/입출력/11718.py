# while True:
#
#     try:
#         N = input()
#         print(N)
#     except:
#         break

import sys

while True:
    N = sys.stdin.readline().rstrip()
    if N == '':
        break
    print(N)