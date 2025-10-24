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
    

    @classmethod 
    def cat_factory(cls, cats):    
        new_cats = [cls(color, age, name) for color, age, name in cats]
        print(new_cats)
        print([cat.speak() for cat in new_cats])
        return new_cats


many_cats = Cat.cat_factory([("black", 9, "Blue"), ("tuxedo", 9, "Patch"),("gray", 15, "Fifi")])
blue, patch, fifi = many_cats
# blue = Cat("black", 9, "Blue")
# patch = Cat("tuxedo", 9, "Patch")
print(blue.name)
print(patch.age)
print(blue.speak())
print(patch.speak())
print(blue.play_with_toy())
