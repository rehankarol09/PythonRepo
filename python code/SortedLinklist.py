#Linklist class to perform operation
#node class having link and data
class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkList(object):
    def __init__(self):
        self.start = None
    #display function
    def display_list(self):
        if self.start is None:
            print("List is Empty")
        else:
            p = self.start
            while p is not None:
                print(p.info, " ", end=" ")
                p = p.link

    def insert_inorder(self, value):
        temp = Node(value)
        if self.start is None or self.start.info>=value:
            temp.link=self.start
            self.start=temp
            return
        p=self.start
        while p.link is not None and p.info<=value:
            p=p.link
        temp.link=p.link
        p.link=temp

    def search(self, value):
        if self.start.info == value:
            print("Your value found at 1")
            return
        p=self.start
        i=1
        while p is not None and p.info<value:
            if p.info==value:
                break
            i=i+1
            p=p.link
        if p is None and p.data!=value:
            print()
        else:
            print("Your value", value, "found at", i , "position")

    def createlist(self):
        n=int(int(input("Enter no Element to be inseted")))
        if n == 0:
            return
        for i in range(n):
            value=int(input("Enter the node vslue"))
            self.insert_inorder(value)

    # end of function
if __name__ == '__main__':
    s=SingleLinkList()
    s.createlist()
    s.display_list()
    while True:
        print("Enter 1 to display List")
        print("Enter 2 to add element")
        print("Enter 3 to search a particular element in a List")
        option=int(input("Enter the option"))

        if option == 1:
            s.display_list()
        elif option == 2:
            value=int(input("Enter the element"))
            s.insert_inorder(value)
            s.display_list()
        elif option==3:
            value = int(input("Enter the element"))
            s.search(value)
            s.display_list()
        elif option == 18:
            break
        else:
            print("Choose correct option")




