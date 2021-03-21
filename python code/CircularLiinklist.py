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

    def insert_at_begining(self, data):
        if self.tail is None:
            return
        temp=Node(data)
        temp.link=self.tail.link
        self.tail.link=temp

    def insert_in_emptylist(self,value):
        temp=Node(value)
        self.tail=temp
        self.tail.link=self.tail

    def insert_at_end(self, value):
        if self.tail is None:
            self.insert_in_emptylist(value)
            return
        temp=Node(value)
        temp.link=self.tail.link
        self.tail.link=temp
        self.tail=temp

    def insert_before_node(self, node_value, value):
        if self.tail is None:
            return
        if self.tail.link.data == node_value:
            temp = Node(value)
            temp.link = self.tail.link
            self.tail.link = temp
            return
        p = self.tail.link
        while True:
            if p.link.data == node_value:
                break
            p = p.link
            if p == self.tail.link:
                break
        if p == self.tail.link:
            print()
        else:
            temp = Node(value)
            temp.link = p.link
            p.link = temp

    def insert_after_node(self, node_value, value):
        if self.tail is None:
            return
        if self.tail.data==node_value:
            temp=Node(value)
            temp.link=self.tail.link
            self.tail.link=temp
            self.tail=temp
            return
        p=self.tail.link
        while True:
            if p.data == node_value:
                break
            p=p.link
            if p==self.tail.link:
                break
        if p==self.tail.link:
            print()
        else:
            temp = Node(value)
            temp.link=p.link
            p.link=temp

    def delete_node(self, value): #todo deletetion with proper logic

        if self.tail is None:
            return
        if self.tail.link.data == value:
            self.tail.link=self.tail.link.link
            return

        p = self.tail.link
        while p.link is not self.tail.link:
            if p.link.data == value:
                break
            p=p.link
        if p.link is self.tail.link:
            print()
        else:
            p.link=p.link.link
            if p.link.data == self.tail.data:
                self.tail=p

    def reverse(self):
       if self.tail is None:
           print("")
           return

       p=self.tail.link
       next=p.link
       while True:
           prev=p
           p=next
           next=p.link
           p.link=prev
           if p == self.tail:
               break
       next.link=self.tail
       self.tail=next

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            print("list is circular")
            return True

    def find_cycle(self):
        if self.tail is None:
            return None
        fastr=self.tail
        slowr=self.tail
        while fastr is not None and fastr.link is not None:
            slowr=slowr.link
            fastr=fastr.link.link
            if slowr == fastr:
                return slowr
        return None
    def createlist(self):
        n=int(input("Enter the number of nodes"))
        if n == 0:
            return
        data=int(input("Enter the node value"))
        self.insert_in_emptylist(data)
        for i in range(n-1):
            data = int(input("Enter the node value"))
            self.insert_at_end(data)


if __name__ == '__main__':
  c=CircularLinkList()
  c.createlist()
  while True:
      print("Choose any option")
      print("Enter 1 to display")
      print("Enter 2 to insert node at beg")
      print("Enter 3 to insert element at end ")
      print("Enter 4 to insert a node before a node")
      print("Enter 5 to insert after a particular node")
      print("Enter 6 to delete a particular node")
      print("Enter 7 to reverse")
      option = int(input("enter your choice"))
      if option == 1:
          c.display()
      elif option == 2:
          value = int(input("Enter the value to be inserted"))
          c.insert_at_begining(value)
          c.display()
      elif option == 3:
          value = int(input("Enter the value to be inserted"))
          c.insert_at_end(value)
          c.display()
      elif option == 4:
          node_value = int(input("enter the node value before you want insert a node"))
          value = int(input("enter the value to be inserted"))
          c.insert_before_node(node_value, value)
          c.display()
      elif option == 5:
          node_value = int(input("enter the node value after you want insert a node"))
          value = int(input("enter the value to be inserted"))
          c.insert_after_node(node_value, value)
          c.display()
      elif option == 6:
          c.display()
          value = int(input("Enter the node value to be deleted"))
          c.delete_node(value)
          c.display()
      elif option == 7:
          c.reverse()
          c.display()
      elif option == 8:
          c.has_cycle()
      elif option == 10:
          break
      else:
          print("get lost")




