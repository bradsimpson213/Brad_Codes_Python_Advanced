# Class Syntax!

class Cat:
    def __init__(self, color, age, name="Kitty"):
        self.color = color
        self.age = age
        self.name = name
        self.toys = ["ball", "toy mouse", "yarn"]


blue = Cat("black", 9, "Blue")
patch = Cat("tuxedo", 9, "Patch")
print(blue.name)
print(patch.age)
