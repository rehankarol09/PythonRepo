class InvalidException(Exception):
    pass
class Student_Record(object):
    def __init__(self, i, name):
        self.student_id=i
        self.student_name=name

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, i):
        self.student_id=i

    def __str__(self):
        return str(self.student_id)+" "+self.student_name


class HashTable(object):
    def __init__(self, tablesize=10):
        self.m=tablesize
        self.n=0
        self.array=[None]*self.m

    def hash1(self, key):
        return key % self.m

    def  insert(self, newrecord):
        key=newrecord.get_student_id()
        h=self.hash1(key)
        location=h
        for i in range(1, self.m):
            if self.array[location] is None or self.array[location].get_student_id() == -1:
                self.array[location]=newrecord
                self.n+=1
                return
            if self.array[location]. get_student_id()==key:
                raise InvalidException("Duplicate value")
            location=(h+i) % self.m
        print("Table is full: value cannot be inserted")

    def searchvalue(self, key):
        h=self.hash1(key)
        location=h
        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id() == key:
                return self.array[location]
            location= (h+i) % self.m
        return None
    def display(self):
        for i in range(self.m):
            print("[", end='');print(i, end='');print("]->", end='')

            if self.array[i] is not None and self.array[i].get_student_id() != -1:
                print(self.array[i])
            else:
                print("__")

    def delete_value(self, key):
        h=self.hash1(key)
        location=h
        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id()== key:
                temp=self.array[location]
                self.array[location].set_student_id(-1)
                self.n-=1
                return temp
            location =(h+i) % self.m
        return None

if __name__ == '__main__':
    size=int(input("Input table size"))
    table=HashTable(size)
    while True:
        print("Enter 1 to insert")
        print("Enter 2 to search")
        print("Enter 3 to display")
        print("Enter 4 to delete")
        choice=int(input("Enter your choice"))
        if choice == 1:
            s_id=int(input("Input student id"))
            name = input("Input name")
            arecord=Student_Record(s_id, name)
            table.insert(arecord)
        elif choice == 2:
            key=int(input("Enter value to search"))
            arecord=table.searchvalue(key)
            if arecord is None:
                print("Value not found")
            else:
                print(arecord)
        elif choice == 3:
            table.display()
        elif choice == 4:

            key = int(input("Enter value to delete"))
            arecord = table.delete_value(key)
            if arecord is None:
                print("Value not found")
            else:
                print("Value deleted", )
        elif choice == 5:
            break
        else:
            print("Wong option")
    print("")



