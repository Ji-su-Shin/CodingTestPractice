## 큐 예제

from collections import deque

queue = deque()
print('1: ',queue)

queue.append(1)
queue.append(2)
queue.append(3)
print('2: ', queue)

queue.popleft()
print('3: ', queue)

queue.reverse()
print('4: ', queue)