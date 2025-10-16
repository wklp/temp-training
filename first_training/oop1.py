class Person():
    def __init__(self, name, age):
        self.name =  name
        self.age = age 
    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")

    
person = Person("Alice", 30)
person.greet()