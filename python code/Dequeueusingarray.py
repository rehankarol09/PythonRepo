class QueueEmpty(Exception):
    pass
class Dequeue:
    def __init__(self,max_size=10):
        self.front=-1
        self.rear=-1
        self.arr=[None]*max_size
    def size(self):
        
