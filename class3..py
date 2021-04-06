class Person:
  def __init__(self, name):
    self.name = name

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("VJK")
p1.myfunc()
