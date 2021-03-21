
#node class having link and data
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

    # end of function

   #count the number of node

    def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.link
        print("The number of nodes :", n)
    #end of function
   #count the number of node
    def search(self, x):
        pos=1
        p=self.start
        while p is not None:
            if p.info == x:
                print(x,"is at found at postition", pos)
                break
            p=p.link
            pos+=1
        else:
            print(x, "value not found")

    # end of function
    #insert element at end
    def insert_at_end(self, data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

    # end of function
   #insert element at begining
    def insert_at_begining(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp

    # end of function
    # insert element at begining
    def insert_after(self, x, data):
        p=self.start
        while p is not None:
            if p.info == x:
                break
            p=p.link
        if p is None:
            print(x,"is not found in a list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
    # end of function

   #insert element before a node
    def insert_at_before(self, x , data):
        if self.start is None:
            return
        if x == self.start.info:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return

        p=self.start
        while p.link is not None:
          if p.link.info == x:
            break
          p=p.link

        if p.link is None:
            print(x, "is not found in a list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

   #insert at a particular position
    def insert_at_position(self,k,data):
        if k==1:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return
        p=self.start
        i=1
        while i<k-1 and p is not None:
            p=p.link
            i=i+1
        if p is None:
            print("you can insert upto ",i,"position")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
    #end of function

    #reverse a list
    def reverse_list(self):
       if self.start is None:
           return
       prev=None
       p=self.start
       while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
       self.start=prev


   #delete first node
    def first_node(self):
        if self.start is None:
            return
        self.start=None

   #delete last node
    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start=None
            return
        p=self.start
        while p.link.link is None:
            p=p.link
        p.link=None

    #delete node at particular position
    def delete_at_position(self,x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info == x:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p=p.link
        if p.link is None:
            print("value not found")
        else:
            p.link=p.link.link
    #end of function

   #sort using bubble
    def bubble_sort(self):
        end=None
        while end != self.start.link:
            p=self.start
            while p.link != end:
                q=p.link
                if p.info>q.info:
                    p.info,q.info=q.info,p.info
                p=p.link
            end=p

    #sort using bubble exchanging link
    def bubblesort_exchanginglink(self):
        end=None
        while end!=self.start.link:
            r=p=self.start
            while p.link!=end:
                q=p.link
                if p.info>q.info:
                    p.link=q.link
                    q.link=p
                    if p!=self.start:
                        r.link=q
                    else:
                        self.start=q
                    p,q,=q,p
                r=p
                p=p.link
            end=p
     #end of function

    #merge 2 list
    def _merge2(self, p1, p2):
        if p1.info<=p2.info:
            startM=p1
            p1=p1.link
        else:
            startM=p2
            p2=p2.link
        pM=startM
        while p1 is not None and p2 is not None:
            if p1.info<=p2.info:
                pM.link=p1
                pM=pM.link
                p1=p1.link
            else:
                pM.link=p2
                pM=pM.link
                p2=p2.link
        while p1 is not None:
            pM.link=p1
            pm=pM.link
            p1=p1.link
        while p2 is not None:
            pM.link=p2
            pM=pM.link
            p2=p2.link
        return startM

   #merge sort
    def mergesort(self):
        self.start= self._mergerecursive(self.start)

    def _mergerecursive(self,list_start):
        if list_start is None or list_start.link is None:
            return list_start
        start1=list_start
        start2=self._divide(list_start)
        start1=self._mergerecursive(start1)
        start2=self._mergerecursive(start2)
        startM=self._merge2(start1,start2)
        return startM

    def _divide(self, p):
        q=p.link.link
        while q is not None and q.link is not None:
            p=p.link
            q=q.link.link
        start2=p.link
        p.link=None
        return start2


   #detecting a cycle
    def has_cycle(self):
         if self.find_cycle() is None:
             return False
         else:
             print("it has cycle")

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        slowr=self.start
        fastr=self.start
        while fastr is not None and fastr.link is not None:
            slowr=slowr.link
            fastr=fastr.link.link
            if slowr==fastr:
                return slowr
        return None

    def remove_cycle(self):
        c=self.find_cycle()
        if c is None:
            return
        print("cycle was found at ", c.info)
        p=c
        q=c
        node_list=0
        while True:
            q=q.link
            node_list=node_list+1
            if p==q:
                break
        print("Total number of node in cycle: ", node_list)

        p=self.start
        length_remaining_list=0
        while p!=q:
            length_remaining_list=length_remaining_list+1
            p=p.link
            q=q.link
        print("Node not in a cycle: ", length_remaining_list)
        total_elements=node_list+length_remaining_list
        print("Total nodes in a list ",total_elements)
        i=1
        for i in range(total_elements-1):
            p=p.link
        p.link=None

    def insert_cycle(self, value):
        if self.start is None:
            return
        px=None
        prev=None
        p=self.start
        while p is not None:
            if(p.info==value):
                px=p
            prev=p
            p=p.link
        if px is not None:
            prev.link=px
        else:
            print("")
   #create listass
    def pivot(self,p):
        p=self.start
        while p.link is not None:
            p=p.plink
        return p

    def createlist(self):
        n=int(input("Enter the number of nodes you want to enter"))
        if n == 0:
            return
        for i in range(n):
            data=int(input("Enter the element to insert"))
            self.insert_at_end(data)
    # end of function

list=SingleLinkList()
list.createlist()

while True:
    print("Enter 1 to display List")
    print("Enter 2 to count number of element in  List")
    print("Enter 3 to search a particular element in a List")
    print("Enter 4 to insert element at end ")
    print("Enter 5 to insert element at begin")
    print("Enter 6 to insert element after a node")
    print("Enter 7 to insert element before a node")
    print("Enter 8 to insert element at particular position")
    print("Enter 9 to reverse list")
    print("Enter 10 to delete last node")
    print("Enter 10 to delete first node")
    print("Enter 12 to delete at particular node")
    print("Enter 13 to sort using bubble sort by exchanging data")
    print("Enter 13 to sort using bubble sort by exchanging link")
    print("Enter 15 to sort using merge sort")
    print("Enter 16 to insert a cycle in a List")
    print("Enter 17 to detect a cycle in a List")
    print("Enter 18 to remove a cycle in a List")
    print("Enter 19 to exit")
    option=int(input("Enter any one of the option to: "))

    if option == 1:
        list.display_list()
        print("\n")
    elif option == 2:
        list.count_nodes()
    elif option == 3:
         x=int(input("Enter the value to search"))
         list.search(x)
    elif option == 4:
        x = int(input("Enter the element to add at the end "))
        list.insert_at_end(x)
    elif option == 5:
        x = int(input("Enter the element to add at begining "))
        list.insert_at_begining(x)
    elif option == 6:
        x = int(input("Enter the element after which node is to be added "))
        data=int(input("Enter The data to be added"))
        list.insert_after(x, data)
        list.display_list()
    elif option == 7:
        x = int(input("Enter the element after which node is to be added "))
        data=int(input("Enter The data to be added"))
        list.insert_at_before(x,data)
        list.display_list()
    elif option == 8:
        k=int(input("Enter the position where you want to insert node"))
        value=int(input("Enter the value to be inserted"))
        list.insert_at_position(k, value)
    elif option == 9:
        list.reverse_list()
        list.display_list()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        list.first_node()
    elif option == 12:
        x=int(input("Delete the element of value"))
        list.delete_at_position(x)
        list.display_list()
    elif option == 13:
        list.bubble_sort()
        list.display_list()
    elif option == 14:
        list.bubblesort_exchanginglink()
        list.display_list()
    elif option == 15:
        list.mergesort()
        list.display_list()
    elif option == 16:
        value=int(input("enter the value "))
        list.insert_cycle(value)
    elif option==17:
        list.has_cycle()
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        break
    else:
        print("wrong option")