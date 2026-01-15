class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nMarks: {self.marks}")

s1 = student("Yash", 20, 80)
s1.display()

print("-----------------")

s2 = student("Raj", 30, 80)
s2.display()