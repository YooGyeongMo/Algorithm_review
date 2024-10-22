# N = int(input())
#
# ill = N%10
# sib = (N%100)//10
# beak = (N//100)%10 # (N%1000)//100
# chun = (N//100)//10 # (N//1000)
#
# print(ill+sib+beak+chun)

N = input()

result = sum(int(digit) for digit in N)

print(result)

