N = int(input())

for i in range(N):
    if i == 0 or i == N-1:
        print(' ' * (N-i-1) + "*"*(2*i+1))
    else:
        print(' '* (N-i-1) + "*" + ' ' * (i*2-1) + "*")