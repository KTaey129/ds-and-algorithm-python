# Using deque
def reverse_first_K_elements(k, q):
    stack = []

    # put first k elements in stack
    for i in range(k):
        stack.append(q.popleft())

    # push the contents of the stack to the back of the queue
    # will be added in reverse due to stack LIFO
    while stack:
        q.append(stack.pop())

    # pop and push elements in queue
    # that should come after first k elements in queue
    for i in range(len(q) - k):
        q.append(q.popleft())

    return q

# Using queue
from queue import Queue

# Function to reverse the first K elements of the Queue
def reverseQueueFirstElements(k, Queue):
    stack = []

    # put the first K elements into a Stack
    for i in range(k):
        stack.append(Queue.get())

    # Enqueue the contents of stack at the back of the queue
    while(stack):
        Queue.put(stack.pop())

    # Remove the remaining elements and enqueue them at the end of the Queue
    for i in range(Queue.qsize() - k):
        Queue.put(Queue.get())
