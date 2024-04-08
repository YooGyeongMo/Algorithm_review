T = int(input())

for _ in range(T):
    stk = []
    isVPS = True
    for i in input():
        if i == '(':
            stk.append(i)
        else:
            if stk > 0:
                stk.pop()
            else:
                isVPS = False

    print('YES' if isVPS else 'NO')
