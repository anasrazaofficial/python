class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Anas")
print(person.name)
person.talk()
