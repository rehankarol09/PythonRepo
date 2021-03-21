class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None
#Linklist class to perform operation
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
    def insert_at_end(self, data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

    def createlist(self):
        n=int(input("Enter the number of nodes you want to enter"))
        if n == 0:
            return
        for i in range(n):
            data=int(input("Enter the element to insert"))
            self.insert_at_end(data)

    def concatenation(self,list2):
        if self.start is None:
            self.start=list2.start
            return
        if list2.start is None:
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=list2.start



if __name__ == '__main__':
    list1=SingleLinkList()
    list2=SingleLinkList()
    list1.createlist()
    list2.createlist()
    list1.concatenation(list2)
    print(" After concetinating ")
    list2.display_list()


