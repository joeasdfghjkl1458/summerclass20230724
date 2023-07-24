import queue

q = queue.Queue(maxsize=0)


q.put(0)
q.put(1)
q.put(2)


print(q.queue)

q.get()

print(q.queue)