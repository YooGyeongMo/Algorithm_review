from collections import deque


N = int(input())
q = deque()

for i in range(1, N+1):
    q.append(i)
    # print(q)
# q = deque(range(1,N+1))

while len(q) > 1: #1개 남을때 까지
        q.popleft()
        q.append(q.popleft())

print(q.popleft())