class QueueEmpty(Exception):
    pass
class node:
    def __init__(self, value):
        self.next=None
        self.prev=None
        self.data=value
class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front == None

    def size(self):
        count=0
        p=self.front
        while p is not None:
                count+=1
                p=p.next
        return count
    def insert_front(self, value):
        temp=node(value)
        if self.is_empty():
            self.front=self.rear=temp
        else:
            temp.next=self.front
            self.front.prev=temp
            self.front=temp
    def insert_at_rear(self, value):
        temp=node(value)
        if self.is_empty():
            self.front=self.rear=temp
        else:
            self.rear.next=temp
            temp.prev=self.rear
            self.rear=temp

    def del_front(self):
        if self.is_empty():
            raise QueueEmpty("Queue is Empty")
        if self.front.next is None:
            self.front=self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
    def del_rear(self):
        if self.is_empty():
            raise QueueEmpty("Queue is Empty")
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.rear=self.rear.prev
            self.rear.next=None

    def display(self):
        if self.front is None:
            print("list is empty")
            return
        p = self.front
        while p is not None:
            print("\n", p.data, " ", end=" ")
            p = p.next
    print()
if __name__ == '__main__': # todo sorting algorithm
 l = Dequeue()
 while True:
      print("Choose any option")
      print("Enter 1 to display")
      print("Enter 2 to insert node at rear")
      print("Enter 3 to insert element at front ")
      print("Enter 4 to delete a node front a node")
      print("Enter 5 to delete after a rear node")
      print("Enter 18 to exit")
      option=int(input("enter your choice"))
      if option == 1:
          l.display()
      elif option == 2:
          value=int(input("Enter the value to be inserted"))
          l.insert_at_rear(value)
      elif option == 3:
          value=int(input("Enter the value to be inserted"))
          l.insert_front(value)
      elif option == 4:
          l.del_front()
      elif option == 5:
          l.del_rear()
          l.display()
      else:
          print(" ")









