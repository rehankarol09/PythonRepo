class InvalidException(Exception):
    pass
class Student(object):
    def __init__(self, i, name):
        self.student_id=i
        self.student_name=name

    def getstudentid(self):
        return self.student_id

    def set_Student_id(self, i):
        self.student_id=i

    def __str__(self):
        return str(self.student_id)+" "+self.student_name

class Node(object):
    def __init__(self, value):
        self.info=value
        self.link=None

class SingleLinklist(object):
    def __init__(self):
        self.start=None

    def insert_at_begining(self, value):
        temp=Node(value)
        temp.link=self.start
        self.start=temp

    def search(self, key):
        p=self.start
        while p is not None:
            if p.info.getstudentid() == key:
                print("Search is successful")
                return p.info
            p=p.link
        else:
            print("Search not unsuccessfull")
            return None

    def display(self):
        if self.start is None:
            print("__")
            return
        p=self.start
        while p is not None:
            print(p.info, " ", end=" ")
            p=p.link
        print(" ")

    def delete_node(self, key):
        if self.start is None:
            print("List is empty")
            return

        if self.start.info.getstudentid() == key:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info.getstudentid() == key:
                break
            p=p.link

        if p.link is None:
            print("Value not found")
        else:
            p.link=p.link.link
        print(" ")

class Hashtable(object):
    def __init__(self,table_size=10):
        self.n=0
        self.m=table_size
        self.array= [None] * table_size

    def hash1(self, key):
        return key%self.m

    def insert_at_hashtable(self, newrecord):
        key=newrecord.getstudentid()
        h=self.hash1(key)

        if self.array[h] is None:
            self.array[h]= SingleLinklist()
        self.array[h].insert_at_begining(newrecord)
        self.n+=1

    def delete_hash(self, key):
        h=self.hash1(key)
        if self.array[h] is not None:
            self.array[h].delete_node(key)
            self.n-=1

    def display_hash_record(self):
        for i in range(self.m):
            print("[", i, "]--", end=' ')
            if self.array[i] is not None:
                self.array[i].display()
            else:
                print("__")


    def search_value(self, key):
        h=self.hash1(key)
        if self.array[h] is not None:
            return self.array[h].search(key)
        return None




#todo:code check adding id amd name
if __name__ == '__main__':
    size=int(input("Input table size"))
    h=Hashtable(size)
    while True:
        print("Enter 1 to insert")
        print("Enter 2 to search")
        print("Enter 3 to display")
        print("Enter 4 to delete")
        choice=int(input("Enter your choice"))
        if choice == 1:
            id=int(input("Enter your id"))
            name=input("Enter student name")
            srecord=Student(id, name)
            h.insert_at_hashtable(srecord)
        elif choice == 2:
            id=int(input("Enter your id"))
            arecord=h.search_value(id)
            if arecord is None:
                print("Search unsuccesfull")
            else:
                print(arecord)
        elif choice == 3:
            h.display_hash_record()

        elif choice == 4:
            id = int(input("Enter your id"))
            h.delete_hash(id)


        elif choice == 5:
            break
        else:
            print("Wong option")
    print("")










