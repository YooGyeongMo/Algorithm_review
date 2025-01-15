a, b = map(int, input().split())

for i in range(b):
    for j in range(a):
        print("*",end='')
    print()

    a, b = map(int, input().split())

    print(("*" * a + "\n") * b)