class TreeException(Exception):
    pass
class Node(object):
    def __init__(self, value):
        self.data=value
        self.lchild=None
        self.rchild=None

class BinaryTree(object):
    def __init__(self):
        self.root=None

    def is_Empty(self):
        return self.root is None

    def insert(self, x):
       p=self.root
       par = None
       while p is not None:
           par = p
           if x<p.data:
               p=p.lchild

           elif x>p.data:
               p=p.rchild
           else:
               print("Duplicate value")
       temp=Node(x)
       if par is None:
           self.root =temp
       elif x<par.data:
           par.lchild=temp
       else:
           par.rchild=temp

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.data, end=" ")
        self._inorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)

if __name__ == "__main__":
    b=BinaryTree()
    a=int(input("Enter the number of elements to be sorted"))
    for i in range(a):
        value=int(input("Enter element"))
        b.insert(value)
    b.inorder()





