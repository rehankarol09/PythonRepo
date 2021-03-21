from definedsizestack import Stack
from Queue_array import Queue
def reverse(st=Stack(4)):
    q=Queue()
    while not st.is_empty():
        q.enqueue(st.peek())
        st.pop()
    while not q.is_empty():
        st.push(q.peek())
        q.dequeue()

s=Stack(4)
s.push('R')
s.push('E')
s.push('A')
s.push('R')
s.display()
reverse(s)
s.display()