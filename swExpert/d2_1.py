T = int(input())

def exponent(N):
    # 밑 값 배열 만들기
    primes = [2, 3, 5, 7, 11]
    # prime은 내가 구하는 지수값
    # 키값을 선정 Value값은 0으로 통일
    # 딕셔너리로 들어감
    exponent = {prime: 0 for prime in primes}

    # a,b,c,d,e 를 구하기 위한 로직
    for prime in primes:
        while N % prime == 0:
            exponent[prime] += 1
            N //= prime

    # 배열을 반환
    return [exponent[prime] for prime in primes]

# 언패킹 연산자 *
for test_case in range(1, T+1):
    N = int(input())
    print(f"#{test_case}",*exponent(N))


    # # 계속해서 나누어 나머지가 1이 남든 나누는 숫자보다 낮은 숫자를 나누면 0이됨
    # while N % 2 == 0:
    #     a += 1
    #     # 한 싸이클에 나눈 몫을 순차적으로 계속 0이 될때까지 반복해주어야하기 때문에 나누고 나온 몫을 담아야함.
    #     N //= 2








