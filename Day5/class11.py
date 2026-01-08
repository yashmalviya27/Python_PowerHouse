# traversing a list in python

# 1st method: using for loop
""" my_list = [10, 20, 30, 40, 50]

for i in my_list:
    print(i) """

print("-----")

# 2nd method: using range and len()
""" for i in range(len(my_list)):
    print(my_list[i]) """

print("-----")

# 3rd method: using while loop
""" i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1 """

# using halper functions from Day4/num_guessin.py:

# help(list)


# now loving the question in the class usin list.

# Question.1: Sum and Average of elements in a list.

"""n = [10,20,30,40]
sum = 0
for i in n:
    sum +=i 

print(f"the sum of the list is: {sum}\navg of the list is {sum/len(n)}") """

# Question.2: Maximum element in the list.
""" n = [25,30,80,9,88,94,75]
max = n[0]
index= 0
for i in range(len(n)):
    if n[i]>max:
        max = n[i]
        index = i

print(f"The max element is: {max}") """

# Question.3: find the seconf largest element in the list.
n = [25,30,80,9,88,94,75]

max1 = n[0]
max2 = n[0]
index1 = 0
index2 = 0

for i in range(len(n)):
    if n[i]>max1:
        max2=max1
        index2 = index1
        max1=n[i]
        index1 = i

print(f"The 2nd max element is: {max2}\nIndex: {index2}")
        
