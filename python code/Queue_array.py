class QueueEmptyerror(Exception):
    pass
class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def enqueue(self,  value):
        self.items.append(value)
    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyerror("Queue is empty")
        return self.items.pop(0)
    def peek(self):
        if self.is_empty():
            raise QueueEmptyerror("Queue is empty")
        return self.items[0]
    def display(self):
        print(self.items)

if __name__ == '__main__':
    qu=Queue()
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
                value = int(input("Enter your value"))
                qu.enqueue(value)
                qu.display()
                print(" ")
            elif option == 2:
                x = qu.dequeue()
                print("Item Dequeue", x)
                qu.display()
                print()
            elif option == 3:
                print("Item at top of list", qu.peek())
                print()
            elif option == 4:
                qu.display()
                print()
            elif option == 5:
                print("Size of Queue", qu.size())
                print()
            elif option == 6:
                break
            else:
                print("Enter the correct option")
                print()
