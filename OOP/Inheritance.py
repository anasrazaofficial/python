class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):
    pass


class Cat(Animal):
    def meow(self):
        print("Meow! Meow!")


dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.meow()
