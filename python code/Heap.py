class HeapExc(Exception):
    pass
class Heap:
    def __init__(self, maxsize=10):
        self.n=0
        self.a=[None]*maxsize
        self.a[0]=9999

    def insert(self,value):
        self.n+=1
        self.a[self.n]=value
        self.restoreup(self.n)

    def restoreup(self, i):
        k=self.a[i]
        iparent=i//2
        while self.a[iparent]<k:
            self.a[i]=self.a[iparent]
            i=iparent
            iparent=i//2
        self.a[i]=k

    def display(self):

        if self.n == 0:
            return
        print("heap size", self.n)
        for i in range(1,self.n+1):
            print(self.a[i])
        print()


if __name__ == '__main__':
    h=Heap(5)
    h.insert(89)
    h.insert(12)
    h.insert(78)
    h.insert(90)
    h.display()
