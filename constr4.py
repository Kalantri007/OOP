class Addition:
    f = 0
    s = 0
    ans = 0

    def __init__(self, f, s):
        self.f = f
        self.s = s

    def display(self):
        print("First number = " + str(self.f))
        print("Second number = " + str(self.s))
        print("Addition of two numbers = " + str(self.ans))

    def calculate(self):
        self.ans = self.f + self.s


obj = Addition(1000, 2000)

obj.calculate()

obj.display()