N, M = map(int, input().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

target_day = day[N - 1] - M
sum_day = day[N - 1] - target_day

for i in range(0, N):
    if i+1 == N:
        break
    sum_day += day[i]

print(f"{yoil[(sum_day-1) % 7]}")

# 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

# 2번째 풀이

day = 0

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ["SUN",'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

N, M = map(int, input().split())

for i in range(N - 1):
    day += month[i]

day = (day + M) % 7

print(yoil[day])

