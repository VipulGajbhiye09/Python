# Classes and objects

class Human:
    def birth(self):
        self.gender=input("Enter gender:")
        self.name=input("Enter name:")
    def intro(self):
        print(f"hi i am a"{self.gender} named {self.name}")

obj = Human()  ##object
obj.birth()
obj.intro()
