from Stack.Stack import Stack
from Stack.Queue import Queue

stack = Stack(3)

stack.push([1,2,3])
stack.push(('a','quick','brown','fox','jumps','over','the','lazy', 'dog'))

stack.count()
stack.peek()

temp = stack.pop()
print(temp)
stack.count()
stack.peek()

stack.push(1)
stack.push(2)
stack.push('my')
stack.push('pleasure')

stack.count()
stack.peek()
temp = stack.pop()
print(temp)


queue = Queue(3)
queue.enqueue(('a','quick','brown','fox','jumps','over','the','lazy', 'dog'))
queue.enqueue([1,2,3])
queue.enqueue(65535)

queue.peek()
queue.enqueue(456)

temp = queue.dequeue()
print(temp)
queue.peek()
