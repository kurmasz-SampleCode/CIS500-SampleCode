
class Animal:
    def describe(self) -> str:
        warm_cold = self.temperature()
        legs = self.legs()
        return f"I am {warm_cold} and have {legs} legs"

    def temperature(self):
        return "It depends"

class Mammal(Animal):
    def temperature(self):
        return "warm-blooded"

    def legs(self):
        return 4

class Reptile(Animal):

    def describe(self):
        animal_desc = super().describe()
        return f"{animal_desc} and lay eggs"

    def temperature(self):
        return "cold-blooded"

    def speak(self):
        return "<silence>"

class Cat(Mammal):
    def speak(self):
        return "Meow"

class Human(Mammal):
    def speak(self):
        return "Hello"

    def legs(self):
        return 2

class Snake(Reptile):
    def speak(self):
        return "Hiss"

    def legs(self):
        return 0

class Gecko(Reptile):
    def speak(self):
        return "Click"

    def legs(self):
        return 4
