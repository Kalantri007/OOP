class Student:

    def __init__(self):
        print("non parametrized constructor")

    def show(self,name):
        print("Hello",name)

student = Student()
student.show("VK")