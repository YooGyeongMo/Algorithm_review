day = 0

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ["SUN",'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

N, M = map(int, input().split())

for i in range(N - 1):
    day += month[i]

day = (day + M) % 7

print(yoil[day])
