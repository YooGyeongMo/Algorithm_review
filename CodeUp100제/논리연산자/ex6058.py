a , b = map(int, input().split())
a = bool(a)
b = bool(b)
print(not(a or b)) # 둘 중에 하나만 트루여도 트루인데 둘중에 하나만 트루여도 폴즈

