from Cat import Cat



class Tiger(Cat):
    def __init__(self, color, age, name, teeth):
        super().__init__(color, age, name)
        self._teeth = teeth
        print(self.speak())


    def speak(self):
        if self.name == "Tony":
            return F"{self.name} says 'They're great!'"
        else:
            return f"{self.name} says 'RAWRRR!'"


    def __repr__(self):
        return f"< Tiger class: {self.name} is an {self._color} tiger >"


    def __str__(self):
        return f"< Tiger class: {self.name} is an {self._color} tiger >"


tony = Tiger("orange", 72, "Tony", 30)
tigger = Tiger("orange", 90, "Tigger", 12)
print(tony)