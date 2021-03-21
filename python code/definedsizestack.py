class StackEmptyError(Exception):
    pass
class StackFullError(Exception):
    pass
class Stack:
    def __init__(self,max_size=10):
        self.item=[None]*max_size
        self.count=0
    def size(self):
        return self.count
    def is_empty(self):
        return self.count==0
    def is_full(self):
        return self.count==len(self.item)

    def push(self, value):
        if self.is_full():
            raise StackFullError("Stack overflow")
        self.item[self.count]=value
        self.count=self.count+1
    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack Underflow")
        x=self.item[self.count-1]
        self.item[self.count-1]=None
        self.count=self.count-1
        return x
    def peek(self):
        return self.item[self.count-1]
    def display(self):
        print(self.item)
if __name__ == '__main__':
    s=Stack(4)
    while True:
        print("Enter 1 element to push")
        print("Enter 2 pop")
        print("Enter 3 to find peak")
        print("Enter 4 display")
        print("Enter 5 to count ")
        option=int(input("Enter your option"))
        print()
        if option == 1:
            value=int(input("Enter your value to push"))
            s.push(value)
            print(" ")
        elif option == 2:
            x=s.pop()
            print("Item poped", x)
            print()
        elif option == 3:
            print("Item at top of list", s.peek())
            print()
        elif option == 4:
            s.display()
            print()
        elif option == 5:
            print("Size of stack",s.size())
            print()
        elif option ==6:
            break
        else:
            print("Enter the correct option")
            print()

