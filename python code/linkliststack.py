class StackEmpty(Exception):
    pass
class Node:
    def __init__(self,value):
        self.link=None
        self.data=value
class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top == None

    def push(self, value):
        temp=Node(value)
        temp.link=self.top
        self.top=temp

    def pop(self):
        if self.is_empty():
            raise StackEmpty("Stack underflow")
        x = self.top.data
        self.top=self.top.link
        return x

    def peak(self):
        return self.top.data

    def size(self):
        if self.is_empty():
            raise StackEmpty("Stack underflow")
        p=self.top
        i=0
        while p is not None:
            i=i+1
            p=p.link
        return i
    def rev(self):
        if self.top is None:
            return



    def display(self):
        if self.is_empty():
            raise StackEmpty("Stack underflow")
        p=self.top
        while p is not None:
            print(p.data," ",end=" ")
            p=p.link
        print()

if __name__ == '__main__':
    s=Stack()
    while True:
        print("Enter 1 element to push")
        print("Enter 2 pop")
        print("Enter 3 to find peak")
        print("Enter 4 display")
        print("Enter 5 to count ")
        print("Enter 6 to exit")
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
            print("Item at top of list", s.peak())
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

