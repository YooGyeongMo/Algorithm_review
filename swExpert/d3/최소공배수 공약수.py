import math

a, b = map(int, input().split())

def lcm(i,j):
    return i*j // math.gcd(i,j)

print("최대 공약수", math.gcd(21,14))
print("최소 공배수", lcm(a,b))




