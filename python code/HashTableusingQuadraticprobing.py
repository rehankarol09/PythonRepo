class InvalidException(Exception):
    pass
class Student_Record(object):
    def __init__(self, i, name):
        self.student_id=i
        self.name=name

    def get_Student_id(self):
        return self.student_id

    def set_Student_id(self, i):
        self.student_id=i

    def __str__(self):
        return  str(self.student_id)+" "+self.name

class HashTable(object):
    def __init__(self, table_size=10):
        self.n=0
        self.m=table_size
        self.array=[None]*table_size

    def hash1(self, key):
        return key%self.m

    def insert_at_hash(self, newrecord):
        key=newrecord.get_Student_id()
        h=self.hash1(key)
        location=h
        for i in range(1, self.m):

            if self.array[location] is None or self.array[location].get_Student_id() == -1:
                self.array[location] = newrecord
                self.n+=1
                return
            if self.array[location].get_Student_id() == key:
                raise InvalidException("Dupliacte value")
                return

            location=(h+i*i)%self.m
        print("Value cannot be inserted")

    def search_value(self, key):
        h=self.hash1(key)
        location=h
        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_Student_id() == key:
                return self.array[location]
            location=(h+i*i)%self.m
        return None

    def delete_value(self, key):
        h=self.hash1(key)
        location=h
        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_Student_id()==key:
                temp=self.array[location]
                self.array[location].set_Student_id(-1)
                self.n-=1
                return temp
            location = (h + i*i) % self.m
        return None




    def display(self):
        for i in range(self.m):
            print("[", i, "]->", end='')
            if self.array[i] is not None and self.array[i].get_Student_id()!=-1:
                print(self.array[i])
            else:
                print("__")


if __name__ == '__main__':
    size=int(input("Input table size"))
    h=HashTable(size)
    while True:
        print("Enter 1 to insert")
        print("Enter 2 to search")
        print("Enter 3 to display")
        print("Enter 4 to delete")
        choice=int(input("Enter your choice"))
        if choice == 1:
            id=int(input("Enter your id"))
            name=input("Enter student name")
            srecord=Student_Record(id, name)
            h.insert_at_hash(srecord)
        elif choice == 2:
            id=int(input("Enter your id"))
            arecord=h.search_value(id)
            if arecord is None:
                print("Search unsuccesfull")
            else:
                print(arecord)
        elif choice == 3:
            h.display()

        elif choice == 4:
            id = int(input("Enter your id"))
            arecord = h.delete_value(id)
            if arecord is None:
                print("----")
            else:
                print("value deleted ")

        elif choice == 5:
            break
        else:
            print("Wong option")
    print("")



