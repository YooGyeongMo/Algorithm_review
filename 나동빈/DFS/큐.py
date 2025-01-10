from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)
queue.append(0)

queue.popleft()
queue.popleft()
print(queue)

queue.reverse() #역순으로 바꾸기
print(queue)