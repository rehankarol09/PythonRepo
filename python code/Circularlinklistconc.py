class Node(object):
    def __init__(self, value):
        self.link=None
        self.data=value

class CircularLinkList(object):
    def __init__(self):
        self.tail=None

    def display(self):
        if self.tail is None:
            print("empty list")
            return

        temp = self.tail.link
        while True:
            print(temp.data, end=" ")
            temp = temp.link
            if temp == self.tail.link:
                break
        print()

    def insert_in_emptylist(self, value):
        temp = Node(value)
        self.tail = temp
        self.tail.link = self.tail

    def insert_at_end(self, value):
        if self.tail is None:
            self.insert_in_emptylist(value)
            return
        temp = Node(value)
        temp.link = self.tail.link
        self.tail.link = temp
        self.tail = temp

    def createlist(self):
        n = int(input("Enter the number of nodes"))
        if n == 0:
            return
        data = int(input("Enter the node value"))
        self.insert_in_emptylist(data)
        for i in range(n - 1):
            data = int(input("Enter the node value"))
            self.insert_at_end(data)

    def concatenation(self,list2):
        if self.tail is None:
            self.tail=list2.tail
            return
        if list2.tail is None:
            return
        p=self.tail.link
        self.tail.link=list2.tail.link
        list2.tail.link=p
        self.tail=list2.tail


if __name__ == '__main__':
    c1=CircularLinkList()
    c2=CircularLinkList()
    c1.createlist()
    c2.createlist()
    print("Before Concataniting")
    c1.display()
    c2.display()
    c1.concatenation(c2)
    print("After concatinating ")
    c2.display()

