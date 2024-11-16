def gcd(A,B):
    if A%B == 0:
        return B
    else:
        return gcd(B,A%B)

print(gcd(192,162))