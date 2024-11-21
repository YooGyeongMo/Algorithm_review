# while True:
#     line = input()
#     if not line:
#         break
#     a, b = map(int,line.split())
#
#
#     print(a+b)

# import sys
#
# for line in sys.stdin:
#     a, b = map(int, line.split())
#
#     print(a+b)

while True:
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break