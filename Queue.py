from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
print(queue.popleft())
print(queue)
print(queue[0])
if len(queue)==0:
    print("Queue is Empty")
else:
    print("Queue is Not Empty")