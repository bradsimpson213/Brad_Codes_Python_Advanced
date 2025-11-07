# Class Syntax!
from random import choice


class Cat:
    breed = "American Short Hair"

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
    

    @staticmethod 
    def human_to_cat_years(human_age):
        if human_age <= 2:
            return human_age * 12.5
        else:
            return 25 + (human_age - 2) * 4
        

    def __repr__(self):
        return f"< Cat class name: {self.name} is a {self.color} cat>"
    

    def __str__(self):
        return f"< Cat class name: {self.name} is a {self.color} cat>"
    

    def __len__(self):
        return self.age
        


many_cats = Cat.cat_factory([("black", 9, "Blue"), ("tuxedo", 9, "Patch"),("gray", 15, "Fifi")])
blue, patch, fifi = many_cats
print(blue)
print(len(blue))


# blue = Cat("black", 9, "Blue")
# patch = Cat("tuxedo", 9, "Patch")
# print(blue.name)
# print(patch.age)
# print(blue.speak())
# print(patch.speak())
# print(blue.play_with_toy())
# print(Cat.human_to_cat_years(5))
# print(blue.human_to_cat_years(blue.age))
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Long Hair"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)
# blue.breed = "Feisty Ninja Cat"
# print(Cat.breed)
# print(blue.breed)
# print(patch.breed)