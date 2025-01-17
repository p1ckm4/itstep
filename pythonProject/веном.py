class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

    def __str__(self):
        return f"{super().__str__()}, Breed: {self.breed}"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, "Cat", age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the furniture!"

    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}"


my_dog = Dog("Buddy", 3, "Golden Retriever")
my_cat = Cat("Whiskers", 2, "Tabby")

print(my_dog)
print(my_dog.make_sound())
print(my_dog.fetch())

print(my_cat)
print(my_cat.make_sound())
print(my_cat.scratch())
