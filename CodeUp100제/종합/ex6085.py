w, h ,b = map(int, input().split())

answer = (w*h*b)/8/1024/1024

print(f"{answer:.2f} MB")