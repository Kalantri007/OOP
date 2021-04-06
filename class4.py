class Title:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        print(self.name)

V = Title("Vyanky")

print(V.change_name("venku"))
