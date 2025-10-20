# Class Syntax!
from random import choice

class Cat:
    def __init__(self, color, age, name="Kitty"):
        self.color = color
        self.age = age
        self.name = name
        self.toys = ["ball", "toy mouse", "yarn"]


    def speak(self):
        return f"{self.name} says, 'Meow!'"
    

    def play_with_toy(self):
        return f"{self.name} plays with their {choice(self.toys)}"
    


blue = Cat("black", 9, "Blue")
patch = Cat("tuxedo", 9, "Patch")
print(blue.name)
print(patch.age)
print(blue.speak())
print(patch.speak())
print(blue.play_with_toy())
