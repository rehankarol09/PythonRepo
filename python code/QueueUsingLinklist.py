class QueueEmpty(Exception):
    pass
class Node:
    def __init__(self,value):
        self.link=None
        self.info=value
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def is_empty(self):
         return self.front == None
    def sizel(self):
        return self.size
    def enqueue(self,value):
        temp=Node(value)
        if self.front is None:
            self.front=temp
            #self.rear=temp
        else:
            self.rear.link=temp
        self.rear=temp
        self.size=self.size+1
    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty("Queue is Empty")
        x=self.front.info
        self.front=self.front.link
        self.size=self.size-1
        return x
    def peek(self):
        if self.is_empty():
            raise QueueEmpty("Queue is Empty")
        return self.front.info
    def display(self):
        p=self.front
        while p is not None:
            print(p.info," ",end= " ")
            p=p.link
        print()

if __name__ == '__main__':
    q=Queue()
    while True:
        print("Enter 1 element to Enqueue")
        print("Enter 2 to dequeue")
        print("Enter 3 to find peek")
        print("Enter 4 to display ")
        print("Enter 5 to size ")
        print("Enter 6 to exit")
        option = int(input("Enter your option"))
        print()
        if option == 1:
            value=int(input("Enter the value to be inserted"))
            q.enqueue(value)
            q.display()
        elif option == 2:
            x=q.dequeue()
            print("Deleted Element is :", x )
            q.display()
        elif option == 3:
            peek=q.peek()
            print("Element at the top of Queue: " , peek)
        elif option == 4:
            q.display()
        elif option == 5:
            y=q.sizel()
            print("Size of Queue", y)
        elif option == 6:
            break
        else:
            print("Enetr corercr option")

