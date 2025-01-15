def solution(n, m):
    lcm = n * m

    while m != 0:
        n, m = m, n % m

    gcd = n

    lcm /= gcd

    return [gcd, int(lcm)]


import math


def solution(n, m):
    return [math.gcd(n, m), (n * m) // math.gcd(n, m)]


import math


def solution(n, m):
    return [math.gcd(n, m), (n * m) // math.gcd(n, m)]


def get_gcd(a):
    gcd_list = []
    for i in range(1, a + 1):
        if a % i == 0:
            gcd_list.append(i)
    return gcd_list


def solution(n, m):
    a_list = get_gcd(n)
    b_list = get_gcd(m)
    c_list = [x for x in a_list if x in b_list]

    gcd = max(c_list) if c_list else 1

    lcm = (n * m) // gcd

    return [gcd, lcm]

