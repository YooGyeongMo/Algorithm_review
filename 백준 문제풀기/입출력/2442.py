N = int(input())

for i in range(1, N * 2, 2):
    print(" " * ((N*2 - i)//2) + "*" * i)
print()
