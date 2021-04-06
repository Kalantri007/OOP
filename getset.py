class GETSET:
    def __init__(self):
        self._age = 0

    def getage(self):
        print("getter method called")
        return self._age

    def setage(self, a):
        print("setter method called")
        self._age = a

    def delage(self):
        del self._age


age = property(getage, setage, delage)

mark = GETSET()

mark.age = 10

print(mark.age)