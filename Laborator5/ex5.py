class Animal:
    def __init__(self,name):
        self.name=name

class Mammal(Animal):
    def __init__(self, name,no_births):
        super().__init__(name)
        self.no_births=no_births
    
    def is_mother(self):
        if self.no_births>0:
            return True
        else:
            return False
    
class Bird(Animal):
    def __init__(self, name,fly):
        super().__init__(name)
        self.fly=fly
    
    def is_flying(self):
        if self.fly:
            return f"{self.name} is a flying bird"
        else:
            return f"{self.name} is not a flying bird"

class Fish(Animal):
    def __init__(self, name,water_type):
        super().__init__(name)
        self.water_type=water_type
    
    def is_swimming(self):
        return f"{self.name} swims in {self.water_type}"
    

mammal_instance = Mammal(name="Dog", no_births=3)
bird_instance = Bird(name="Eagle", fly=True)
fish_instance = Fish(name="Goldfish", water_type="freshwater")

print(f"{mammal_instance.name} is a mammal: {mammal_instance.is_mother()}")

print(bird_instance.is_flying())

print(fish_instance.is_swimming())
