import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


def lcm2(a, b):
    answer = a * b
    while b != 0:
        a, b = b, a % b
    return answer // a


def solution(numer1, denom1, numer2, denom2):
    common_denom = lcm(denom1, denom2)
    common_numer = numer1 * (common_denom // denom1) + numer2 * (common_denom // denom2)
    value = math.gcd(common_numer, common_denom)
    return [common_numer // value, common_denom // value]

# 다른 풀이

import math


def solution(numer1, denom1, numer2, denom2):
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2

    gcd_value = math.gcd(boonja, boonmo)
    boonmo //= gcd_value
    boonja //= gcd_value

    return [boonja, boonmo]
