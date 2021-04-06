class emp:
    def __init__(self):
        self.name = 'xyz'
        self.salary = 4000
        v1 = emp.show(self.name)

    def show(self):
        print(self.name)
        print(self.salary)


e1 = emp()
print("Dictionary form :", vars(e1))

# var = displays attributes of instance in dict form
