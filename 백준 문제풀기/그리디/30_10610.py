# 30의 배수를 찾자
# 3과 10의 배수여야함, 3은 각자리 수 합이 3의 배수일때와 10의 배수는 끝자리가 0 이어야함.
# 10^5 승 개 숫자면 int형은 어려움 정렬로 해도 시간 너무 오래걸림
# 스트링으로 잘랐다가 출력시에 다시 붙이기

N = input()

a_list = [int(i) for i in N]

sum = 0

a_list.sort(reverse=True)

for i in a_list:
    sum += i

if sum % 3 == 0 and 0 in a_list:
    for i in a_list:
        print(i,end='')

else:
    print(-1)