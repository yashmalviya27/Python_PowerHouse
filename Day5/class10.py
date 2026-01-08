# list in python
""" my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

my_list.pop(2)
print(my_list)

my_list.remove(4)
print(my_list) """


# refrence vs shallow copy vs deep copy.
# this is refrencr
# in which both a and b point to same memory location
a= [1,2,3,4,5]
b= a
b[0]= 100
print(f"b: {b} a: {a}") # b: [100,2,3,4,5] a: [100,2,3,4,5] (refrence) (a)

# shallow copy in which both a and b point to different memory location
shallow_copy = a.copy()
shallow_copy[1] = 200
print(f"shallow_copy: {shallow_copy} a: {a}") # shallow_copy: [1, 200, 3, 4, 5] a: [1, 200, 3, 4, 5] (shallow_copy)

# Deep copy in which both a and b point to different memory location
import copy
deep_copy = copy.deepcopy(a)
deep_copy[2] = 300
print(f"deep_copy: {deep_copy} a: {a}") # deep_copy: [1, 2, 300, 4, 5] a: [1, 2, 3, 4, 5] (deep_copy)



