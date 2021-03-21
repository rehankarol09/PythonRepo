from dequeueusingdoublelinklist import Dequeue
class TreeException(Exception):
    pass
class Node:
    def __init__(self, value):
        self.lchild=None
        self.rchild=None
        self.data=value
class BinaryTree:
    def __init__(self):
        self.root=None
    def is_empty(self):
        return self.root == None

    def insertinnode(self, x):
        p=self.root
        par=None
        while p is not None:
            par=p
            if x<p.data:
                p=p.lchild
            elif x>p.data:
                p=p.rchild
            else:
                print(x, " Already present in tree")
                break
        temp=Node(x)
        if par == None:
            self.root=temp
        elif x<par.data:
            par.lchild=temp
        else:
            par.rchild=temp

    def search_iterative(self, x):
        p = self.root
        while p is not None:
            if x < p.data:
                p = p.lchild
            elif x > p.data:
                p = p.rchild
            else:
                return True
        return False

    def display(self):
        self._display(self.root, 0)

    def _display(self, p, level):
        if p is None:
            return
        self._display(p.rchild, level+1)
        print()
        for i in range(level):
            print(" ", end=" ")
        print(p.data)
        self._display(p.lchild, level+1)

    def preorder(self):
        self._preorder(self.root)
        print()
    def _preorder(self, p):
        if p is None:
            return
        print(p.data, " ", end=" ")
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.data, " ", end=" ")
        self._inorder(p.rchild)
    def inorder(self):
        self._inorder(self.root)
        print(" ")

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.data, " ", end=" ")

    def postorder(self):
        self._preorder(self.root)
        print(" ")

    def deletenode(self, x):
        p=self.root
        par=None
        ch=None
        while p is not None:
            if x==p.data:
                break
            par=p
            if x<p.data:
                p=p.lchild
            else:
                p=p.rchild
        if p is None:
            print("Element not found")
            return
        if p.lchild is not None and p.rchild is not None:
            ps=p
            s=p.rchild
            while s.lchild is not None:
               ps=s
               s=s.lchild
            p.info=s.info
            par=ps

        if p.lchild is not None:  #
            ch=p
        elif p.rchild is not None:  #
            ch=p
        if par is None:       #
            self.root=ch
        elif p == par.lchild:  #
            par.lchild=ch
        else:                 #
            par.lchild=ch

    def _height(self, p):
        if p is None:
            return 0
        hl=self._height(p.lchild)
        hr=self._height(p.rchild)
        if hl > hr:
            return 1+hl
        else:
            return 1+hr
    def height(self):
        return self._height(self.root)
    def minimum(self):
        if self.is_empty():
            raise TreeException("tree is empty")
        p=self.root
        while p.lchild is not None:
            p=p.lchild
        print("Minimum value", p.data)
    def max(self):
        if self.is_empty():
            raise TreeException("tree is empty ")
        p=self.root
        while p.rchild is not None:
            p=p.rchild
        print("Max value", p.data)



if __name__ == '__main__':
    bst=BinaryTree()
    while True:
        print("Choose any option")
        print("Enter 1 to display")
        print("Enter 2 to insert a node ")
        print("Enter 3 to find preorder")
        print("Enter 4 to find postorder")
        print("Enter 5 to find inorder")
        print("Enter 6 to search ")
        print("Enter 7 to delete")
        print("Enter 8 to find height of tree")
        print("Enter 9 to find max value")
        print("Enter 10 to find min value")
        print("Enter 18 to exit")
        option = int(input("enter your choice"))
        if option == 1:
            bst.display()
        elif option == 2:
            value = int(input("Enter the value to be inserted"))
            bst.insertinnode(value)
        elif option == 3:
            bst.preorder();
        elif option == 4:
            bst.postorder()
        elif option == 5:
            bst.inorder()
        elif option == 6:
            value = int(input("Enter the value to be search"))
            if bst.search_iterative(value):
                print(" Key found")
            else:
                print("Key not found")
        elif option == 7:
            value = int(input("Enter the value to be delted"))
            bst.deletenode(value)
        elif option == 8:
            x = bst.height()
            print("Height of tree", x)
        elif option == 9:
            bst.max()
        elif option == 10:
            bst.minimum()

        else:
            print(" ")




