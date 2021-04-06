class C(object):
    clsAtr = "class Attribute"

obj1 = C()
obj2 = C()

print(obj1.clsAtr)
C.clsAtr = "New class Attribute"

print(obj2.clsAtr

# how to change change class attribute