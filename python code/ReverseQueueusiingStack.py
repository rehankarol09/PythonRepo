from definedsizestack import Stack
from Queue_array import Queue
def reverse(q=Queue()):
    st=Stack()
    while not q.is_empty():
        st.push(q.peek())
        q.dequeue()
    while not st.is_empty():
        q.enqueue(st.peek())
        st.pop()
s=Queue()
s.enqueue(11)
s.enqueue(22)
s.enqueue(33)
s.display()
reverse(s)
s.display()

