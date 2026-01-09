# tuple in Python

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Access time complexity: O(1)
# Space complexity: O(n)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# accessing tuple elements
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# tuple unpacking (correct)
a, b, *c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]

# concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# tuple methods
print(my_tuple.count(2))  # 1
print(my_tuple.index(3))  # 2

# immutability of tuples
temp_list = list(my_tuple)
temp_list[0] = 10
my_tuple = tuple(temp_list)
print(my_tuple)  # (10, 2, 3, 4, 5)
# trying to change an element directly will raise an error
# my_tuple[0] = 10  # This will raise a TypeError

# tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)
tuple4 = tuple1 * 3
print(tuple4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(2 in my_tuple)  # True
print(len(my_tuple))  # 5
for item in my_tuple:
    print(item)

my_tuple.count(2)
my_tuple.index(3)