class Get:
    def __init__(self):
        self._name = 0

    @property
    def age(self): #getter
        return self._name

    @age.setter  # setter
    def age(self, a):
        if a == "VJK":
            print("ACCESS GRANTED")
        print("Not Granted")
        self._name = a


mark = Get()

mark.name = "PK"

print(mark.name)