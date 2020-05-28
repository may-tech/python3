class Student:
    def __init__(self, name):
        self.name = name
        print(self.name)

    def avg(self, math,  english):
        print((math + english)/2)

a001 = Student("may")
#print(a001.name)
a001.avg(90, 80)

a002 = Student("python")
#print(a002.name)
a002.avg(30, 100)


