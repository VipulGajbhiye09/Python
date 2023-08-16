Inheritance Abstraction Polymorphism Encapsulation are the 4 core concepts of OOP

# Inheritance Example 

class Employee:
    def __init__(self,name,id):   
        self.name = name
        self.id = id
      
    def details(self):
        print(f"Name is {self.name} with id {self.id}")

class Programmer(Employee):      # class Programmer inherited class Employee properties
    def language(self):
        print("Language used is python")

e1 = Employee("Rohan",1)

e2 = Programmer("Vipul",2)
