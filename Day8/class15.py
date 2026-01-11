# lambda expression
# lambda function
# lambda function is also called anonymous function
# is me jo be choto function hai us me koi bhi name nahi hai
square = lambda x: x**2
add = lambda x, y: x + y
print(square(5))
print(add(5, 10))

# map function
# purpose of map function is to apply a function to each element of a sequence and return a new sequence
# map function is used to apply a function to each element of a sequence and return a new sequence

# syntax: map(function, sequence)
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# filter function
# filter function is used to filter elements of a sequence based on a condition
# syntax: filter(function, sequence)
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# zip function
# zip function is used to combine multiple sequences into a single sequence of tuples
# syntax: zip(sequence1, sequence2)
names = ["John", "Jane", "Jack"]
ages = [25, 30, 35]
zipped = dict(list(zip(names, ages)))
print(zipped)

# reduce function
# reduce function is used to apply a function to a sequence of elements and return a single value
# syntax: reduce(function, sequence)
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

a = [1,2,3,4,5,6,7,8,9,10]
l = [i for i in a if i%2==0]
s = [i for i in a if i%2!=0]
d = {i:i+i for i in a}
print(l)
print(s)
print(d)

# generator and decorator