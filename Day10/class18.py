#class and object in python

# class is the blueprint of object and object is the instance of class

# class 
# this is the class-----
class car:

    def __init__(self, mark, model, year):
        # self is use for object variable and class variable use to store data
        
        # this is an constructor
        self.mark = mark
        self.model = model
        self.year = year
    # this is a method/function
    def info(self):
        print(f"car mark is: {self.mark}\n car model is: {self.model}\n car year is: {self.year}")

# this is an object
c1 = car("Honda", "Civic", 2022)
c1.info()

c2 = car("Toyota", "Camry", 2021)
c2.info()
#class and object in python

# class is the blueprint of object and object is the instance of class

# class 
# this is the class-----
class car:

    def __init__(self, mark, model, year):
        # self is use for object variable and class variable use to store data
        
        # this is an constructor
        self.mark = mark
        self.model = model
        self.year = year
    # this is a method/function
    def info(self):
        print(f"car mark is: {self.mark}\n car model is: {self.model}\n car year is: {self.year}")

# this is an object
c1 = car("Honda", "Civic", 2022)
c1.info()

c2 = car("Toyota", "Camry", 2021)
c2.info()