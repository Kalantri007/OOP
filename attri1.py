class A (object):
    clAtr = "same for all"

    def __init__ (self, insAtr):
        self.insAtr = insAtr

obj1 = A(123)
obj2 = A(456)

print("OBJECT 1 Attributes ")
print("class Attribute", obj1.clAtr)
print("instance Attribute", obj1.insAtr)
print()
print("OBJECT 2 Attributes ")
print("class Attribute", obj2.clAtr)
print("instance Attribute", obj2.insAtr)

v1 = A(1)
v1.clAtr = "abc"
print(v1.clAtr)
print(A.clAtr)
# differnce between class and instance attribute