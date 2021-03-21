class Node(object):
    def __init__(self,value):
        self.prev=None
        self.next=None
        self.data=value

class Doublelinklist(object):
    def __init__(self):
        self.start=None
    def display(self):
        if self.start is None:
            print("list is empty")
            return
        p=self.start
        while p is not None:
            print(p.data," ",end=" ")
            p=p.next

    def insert_at_end(self,value):
        temp=Node(value)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        temp.prev=p
        p.next=temp

    def insert_at_begining(self,value):
        temp=Node(value)
        if self.start is None:
            self.start=temp
            return
        temp.next=self.start
        self.start.prev=temp
        self.start=temp

    def insert_before_node(self,node_value,value):
        temp=Node(value)
        if self.start.data == node_value:
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return
        p=self.start
        while p is not None:
            if p.data == node_value:
              break
            p=p.next
        if p is None:
            print("value not found")
        else:
           temp.next=p
           temp.prev=p.prev.next
           p.prev.next=temp
           p.prev=temp

    def insert_after_node(self,node_value,value):
        temp=Node(value)
        if self.start is None:
            return
        if self.start.data == node_value:
            temp.next=self.start.next
            temp.prev=self.start
            self.start.next=temp
            self.start.next.prev=temp
            return
        p=self.start
        while p is not None:
            if p.data == node_value:
               break
            p=p.next
        if p is  None:
            print("")
        elif p.next is None:
            temp.prev=p.next
            p.next=temp
        else:
            temp.next=p.next
            temp.prev=p
            p.next.prev=temp
            p.next=temp

    def delete_node(self,value):
        if self.start is None:
            return

        if self.start.data == value:
           self.start=self.start.next
           return
        p=self.start
        while p is not None:
            if p.data==value:
                break
            p=p.next
        if p is  None:
            print("")
        elif p.next is None:
            p.prev.next=None
        else:
            p.prev.next=p.next
            p.next.prev=p.prev

    def reverse(self):
        if self.start is None:
            return
        if self.start.next is None:
            return
        p1=self.start
        p2=p1.next
        p1.prev=p2
        p1.next=None
        while p2 is not None:
            p2.prev=p2.next
            p2.next=p1
            p1=p2
            p2=p2.prev
        self.start=p1


#_____________Quicksort_______________
    #swap

    #partition
    def partition(self, low, high):
        i=low.prev
        pivot=high
        j=low
        while j != high:
            if j.data<=pivot.data:
                if i is  None:
                   i=low
                   i.data, j.data=j.data,i.data
                   j=j.next
                else:
                    i=i.next
                    i.data, j.data=j.data,i.data
                    j=j.next
            else:
                j=j.next
        if i is None:
          i=low
          i.next.data, high.data=high.data,i.next.data
        return i

    def _quicksort(self, low, high):
        if low==high:
            return
        pi=self.partition(low, high)
        self._quicksort(low, pi.prev)
        self._quicksort(pi.next, high)

    def last_node(self, h):
        h=self.start
        while h and h.next:
            h=h.next
        return h

    def quicksort(self):
        last_node1=self.last_node(self.start)
        self._quicksort(self.start, last_node1)

    def createlist(self):
            n = int(input("enter the number of nodes "))
            if n == 0:
                return
            for i in range(n):
                data = int(input("Enter the value"))
                self.insert_at_end(data)
            self.display()

    # driver code
if __name__ == '__main__': # todo sorting algorithm
 l = Doublelinklist()
 l.createlist()
 while True:
      print("Choose any option")
      print("Enter 1 to display")
      print("Enter 2 to insert node at beg")
      print("Enter 3 to insert element at end ")
      print("Enter 4 to insert a node before a node")
      print("Enter 5 to insert after a particular node")
      print("Enter 6 to delete a particulsr node")
      print("Enter 7 to reverse a list")
      print("Enter 18 to exit")
      option=int(input("enter your choice"))
      if option == 1:
          l.display()
      elif option == 2:
          value=int(input("Enter the value to be inserted"))
          l.insert_at_begining(value)
      elif option == 3:
          value=int(input("Enter the value to be inserted"))
          l.insert_at_end(value)
      elif option == 4:
          node_value=int(input("enter the node value before you want insert a node"))
          value=int(input("enter the value to be inserted"))
          l.insert_before_node(node_value,value)
      elif option == 5:
          node_value = int(input("enter the node value after you want insert a node"))
          value = int(input("enter the value to be inserted"))
          l.insert_after_node(node_value,value)
      elif option == 6:
          value=int(input("Enter the node value to be deleted"))
          l.delete_node(value)
          l.display()
      elif option == 7:
          l.reverse();
          l.display()
      elif option == 8:
          l.quicksort()
          l.display()
      elif option == 18:
          break
      else:
          print(" ")
