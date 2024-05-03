# N = int(input())
#
# ill = int(N%10)
# sib = int((N//10)%10)
# baek = int((N//100)%10)
# chun = int((N//1000)%10)
# result = sum([ill, sib, baek, chun])
# print(result)

N = int(input())

result = sum(int(digit) for digit in str(N))
#sum()함수는 리스트로 발생
#for 변수 in str(N) 하면 변수에 문자열을 for문 돌면서 문자로 쪼개어 저장함

print(result)