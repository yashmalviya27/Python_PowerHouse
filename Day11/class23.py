# inheritance in python
# Inheretance is a way to creat a new class for a class which is already exist
# It is the process whare one child class is having the feature of parent class

# this is the single level inheritance
""" class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        super().display()
        print(f"Grade: {self.grade}")

c1 = Child("Yash", 20, "A")
c1.display()

p1 = Parent("Ashish", 30)
p1.display() """


# now this is the multiple level inheritance

"""class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class human(animal):
    def __init__(self, name, age, gender):
        super().__init__(name , age)
        self.gender = gender

    def display(self):
        super().display()
        print(f"Gender: {self.gender}")

class robots(human):
    def __init__(self, name, age, genger, ID):
        super().__init__(name , age, genger)
        self.ID = ID

    def display(self):
        super().display()
        print(f"ID: {self.ID}")


r1 = robots("Yash", 20, "Male", 123)
r1.display() """