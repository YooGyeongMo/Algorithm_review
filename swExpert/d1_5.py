N = int(input())

m = list(map(int, input().split()))
m.sort()
print(m[round(N/2)-1:round(N/2)][0])