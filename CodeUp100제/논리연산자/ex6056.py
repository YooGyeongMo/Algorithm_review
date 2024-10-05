a, b = map(int, input().split())
a = bool(a)
b = bool(b)


print(((not a) and b) or (a and (not b)))

print(a!=b)

print(a and b)
print(a == b)