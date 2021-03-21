class Queueempty(Exception):
    pass
class Queue:
    def __init__(self, max_size=7):
        self.front=0
        self.count=0
        self.items=[None]*max_size
    def is_empty(self):
        return self.count==0
    def size(self):
        return self.count
    def enqueue(self,value):
        if self.count==len(self.items):
            self.resize(2*len(self.items))

        i=(self.front+self.count)%len(self.items)
        self.items[i]=value
        self.count=self.count+1
    def dequeue(self):
        if self.is_empty():
            raise Queueempty("Queue is empty")
        x=self.items[self.front]
        self.items[self.front]=None
        self.front=(self.front+1)%len(self.items)
        self.count=self.count-1
        return x
    def peek(self):
        if self.is_empty():
            raise Queueempty("Queue is empty")
        return self.items[self.front]
    def display(self):
        print(self.items)
    def resize(self,new_size):
        oldlist=self.items
        self.items=[None]*new_size
        i=self.front
        for j in range(self.count):
            self.items[j]=oldlist[i]
            i=(i+1)%len(oldlist)
        self.front=0

if __name__ == '__main__':
    qu=Queue(7)
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

