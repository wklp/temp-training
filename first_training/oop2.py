class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("The animal makes a sound.")   
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print(f"Woof! My name is {self.name}")
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print(f"Meow! I’m {self.name} and I’m a cat.") 

dog = Dog("Buddy")
cat = Cat("tot")
animal = Animal("Animal")
dog.speak()
cat.speak()
animal.speak()