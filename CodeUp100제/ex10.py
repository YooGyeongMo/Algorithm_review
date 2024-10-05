y, m, d = input().split('.')
print(d,m,y,sep='-')

time = input().split('.')
time = reversed(time)
print('-'.join(time))