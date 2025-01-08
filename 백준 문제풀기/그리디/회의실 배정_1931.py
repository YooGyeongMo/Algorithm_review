import sys

N = int(input())

arr = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    arr.append([start, end])

arr.sort(key= lambda x:(x[1],x[0])) #끝나는 시간 기준, 끝나는 시간이 같을때는 시작시간 기준으로


end_time = arr[0][1]

room_cnt = 1

for i in range(1,N):
    if end_time <= arr[i][0]:
        room_cnt += 1
        end_time = arr[i][1]

print(room_cnt)