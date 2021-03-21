class QueueEmpty(Exception):
    pass
class Node:
    def __init__(self,value):
        self.link=None
        self.info=value
class Queue:
    def __init__(self):
        self.rear=None
        self.size=0
    def is_empty(self):
        return self.rear == None

    def Enqueue(self,value):
        temp=Node(value)
        if self.rear is None:
            self.rear=temp
            self.rear.link=self.rear
        else:
           temp.link=self.rear.link
           self.rear.link=temp
           self.rear=temp
    def sizel(self):
        if self.is_empty():
            raise QueueEmpty(" ")
        n=0
        p=self.rear.link
        while True:
            n=n+1
            p=p.link
            if p == self.rear.link:
                break
        return n
    def Dequeue(self):
        if self.is_empty():
            raise QueueEmpty("Queue is Empty")
        if self.rear.link == self.rear:
            x=self.rear.info
            self.rear=None
        else:
            x = self.rear.link.info
            self.rear.link = self.rear.link.link
        return x
    def peek(self):
        if self.is_empty():
            raise QueueEmpty("Queue is Empty")
        if self.rear.link == self.rear:
            x=self.rear.info
        else:
            x=self.rear.link.info
        return x
    def display(self):
        if self.rear is None:
            print("Queue is Empty")
            return
        p=self.rear.link
        while True:
            print(p.info, " ", end=" ")
            p=p.link
            if p==self.rear.link:
                break
        print(" ")


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
            q.Enqueue(value)
            q.display()
        elif option == 2:
            x=q.Dequeue()
            print("Deleted Element is :", x )
        elif option == 3:
            peek=q.peek()
            print("Element at the top of Queue: " , peek)
        elif option == 4:
            q.display()
        elif option == 5:
            p=q.sizel()
            print("Size of Queue", p)
        elif option == 6:
            break
        else:
            print("Enter correct option")
