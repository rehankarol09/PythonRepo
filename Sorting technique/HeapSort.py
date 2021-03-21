class HeapException(Exception):
    pass

class HeapSort:
    def __init__(self, size=10):
        self.n=0
        self.a=[None]*size
        self.a[0]=999999

    def insert(self, value):
        self.n+=1
        self.a[self.n]=value
        self.restoreup(self.n)

    def restoreup(self, i):
        k=self.a[i]
        iparent=i//2
        while self.a[iparent] <k:
            self.a[i]=self.a[iparent]
            i=iparent
            iparent=i//2
        self.a[i]=k

    def delete_node(self):
        if self.n == 0:
            raise HeapException("Heap is empty")
            return
        maxvalue=self.a[1]
        self.a[1]=self.a[self.n]
        self.n-=1
        self.restoreDown(1)
        return maxvalue

    def restoreDown(self, i):
        k=self.a[i]
        lchild=2*i
        rchild=lchild+1

        while rchild <= self.n:
            if k>=self.a[lchild] and k>=self.a[rchild]:
                self.a[i]=k
                return
            else:
                if self.a[lchild]>self.a[rchild]:
                    self.a[i]=self.a[lchild]
                    i=lchild
                else:
                    self.a[i]=self.a[rchild]
                    i=rchild
            lchild=2*i
            rchild=lchild*i*i
        if lchild==self.n and k>=self.a[lchild]:
            self.a[i]=self.a[lchild]
            i=lchild
        self.a[i]=k




    def display(self):

        if self.n == 0:
            return
        print("heap size", self.n)
        for i in range(1, self.n+1):
            print(self.a[i])
        print()


if __name__ == '__main__':
    temp=[None]*5
    h=HeapSort(5)
    h.insert(11)
    h.insert(23)
    h.insert(55)
    h.insert(63)



