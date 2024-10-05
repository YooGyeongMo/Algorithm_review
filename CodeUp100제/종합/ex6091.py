## 브루트 포스 입력값 커지면 부하 큼

# a, b, c = map(int,input().split())
#
# d = 1
#
# while d%a != 0 or d%b != 0 or d%c != 0:
#     d +=1
#
# print(d)

# 유클리드 호제법으로 두 수의 최대 공약수를 구하고 두 수 곱을 최대 공약수로 나누면됨.

numbers = list(map(int,input().split()))

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)

def list_lcm(num_list):
    result = num_list[0]
    for i in range(1, len(num_list)):
        result = lcm(result,num_list[i])
    return result

print(list_lcm(numbers))