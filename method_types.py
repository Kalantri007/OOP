from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def Aged(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def Vote(age):
        return age > 18


person1 = Person('VK', 21)
person2 = Person.Aged('PK', 1999)

print(person1.age)
print(person2.age)

print(Person.Vote(22))