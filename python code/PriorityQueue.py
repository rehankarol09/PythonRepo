class QueueEmpty(Exception):
    pass
class Node(object):
    def __init__(self, priority, value):
        self.link=None
        self.priority = priority
        self.info=value

class Queue:
    def __init__(self):
        self.front=None

    def is_empty(self):
       return self.front == None

    def enqueue(self, priority, value):
        temp=Node(priority, value)
        if self.front is None:
            self.front=temp
        elif self.front.priority<priority:
            temp.link=self.front
            self.front=temp
        else:
            p=self.front
            while p.link is not None and p.link.priority>=priority:
                p=p.link
            if p is None:
                p.link=temp
            else:
                temp.link=p.link
                p.link=temp
    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty("QUEUE is Empty")
        x=self.front.priority
        self.front=self.front.link
        return x


    def display(self):
        if self.is_empty():
            raise QueueEmpty("QUEUE is Empty")
        p=self.front
        while p is not None:
            print("|", p.priority, "|", p.info, "|", " ->", end=" ")
            p=p.link
        print()


if __name__ == '__main__':
    q=Queue()
    q.enqueue(5,1)
    q.enqueue(6,3)
    q.enqueue(4,3)
    q.enqueue(11,3)
    q.enqueue(4,5)
    q.enqueue(11,8)
    q.display()
    while True:
        print("Enter 1 to dequeue")
        option=int(input("Enter your option "))
        if option == 1:
            x = q.dequeue()
            print("Element deque with priority", x)
            q.display()
        elif option==2:
            break
        else:
            print("Get lost")




