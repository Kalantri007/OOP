class Get:
    def __init__(self):
        self._age = 0

    @property
    def age(self): #getter
        print("getter method called")
        return self._age

    @age.setter  # setter
    def age(self, a):
        if (a < 18):
            print("Not for vote")
        print("setter method called")
        self._age = a


mark = Get()

mark.age = 19

print(mark.age)