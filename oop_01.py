# Classes and objects

# Class is a blueprint/template for creating objects.
# It defines properties and methods that an objecct of that class will have.

# object is an instance of the class

class Human:
    def birth(self):   
        self.gender=input("Enter gender:")
        self.name=input("Enter name:")
    def intro(self):
        print(f"Hi I'm a {self.gender} named {self.name}")

# self is a reference to current instance of the class

obj = Human()  ##object created
obj.birth()
obj.intro()

##Constructor is a special method that is automatically invoked when object of that class is created
##Constructor is used to initialize an object

# Parameterized constructor
class Human:
    def __init__(self,name,gender):  ##Constructor
        print("init called:")
        self.gender=gender
        self.name=name
        print(f"Hi I'm a {self.gender} named {self.name}")

obj2 = Human("vipul","male")  ##object created
## Constructor will be invoked here
