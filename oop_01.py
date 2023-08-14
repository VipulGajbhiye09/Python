# Classes and objects

class Human:
    def birth(self):
        self.gender=input("Enter gender:")
        self.name=input("Enter name:")
    def intro(self):
        print(f"Hi I'm a {self.gender} named {self.name}")

obj = Human()  ##object
obj.birth()
obj.intro()

##Constructor is a special method that is automatically invoked when object of that class is created
##Constructor is used to initialize an object

class Human:
    def __init__(self,name,gender):  ##Constructor
        print("init called:")
        self.gender=gender
        self.name=name
        print(f"Hi I'm a {self.gender} named {self.name}")
