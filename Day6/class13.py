# set in Python
# in this i cant add duplicate values
# unOrdered_collection and nature of set is unordered
# set don't allow indexing. it does not have any indexing
# set is mutable we can add or remove values        
my_set = {10, 2, 30, 10, 4, 5}
print("Original set:", my_set)

# adding value to set
my_set.add(20)
print("Set after adding value:", my_set)

# removing value from set
my_set.remove(2)
print("Set after removing value:", my_set)

# checking membership
print("Is 30 in set?", 30 in my_set)
print("Is 40 in set?", 40 in my_set)

# set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)

# set construction from list
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set_from_list = set(my_list)
print("Set constructed from list:", my_set_from_list)

# set traversal
print("Traversing set:")
for value in my_set:
    print(value)

