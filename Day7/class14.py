# Dictionary in Python

# A dictionary is a collection which is unordered, changeable and indexed.
# Dictionaries are written with curly brackets, and they have keys and values.
# Access time complexity: O(1)
# Space complexity: O(n)

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
print(my_dict["name"])

for i in my_dict:
    print(i)

print("-------")

for i in my_dict.values():
    print(i)

print("-------")

for i in my_dict.keys():
    print(i)

print("-------")

a = dict()
a["name"] = "Yash"
a["age"] = 20
a["city"] = "Pune"
print(a)

print("-------")

a = dict(name="Yash", age=20, city="Pune")
print(a)

print("-------")

a.pop("name")
print(a)

print("-------")

a.popitem()
print(a)

print("-------")

a.clear()
print(a)

# upadte
a.update({"name": "Yash", "age": 20, "city": "Pune"})
print(a)