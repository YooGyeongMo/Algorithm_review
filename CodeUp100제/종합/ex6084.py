h, b, s, c = map(int, input().split())

answer = (h*b*s*c)/8/1024/1024

print(f'{answer:.1f} MB')