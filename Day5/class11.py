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
""" n = [25, 30, 80, 9, 94, 75, 88]

max1 = n[0]
max2 = n[0]
index1 = 0
index2 = 0

for i in range(len(n)):
    if n[i] > max1:
        max2 = max1
        index2 = index1

        max1 = n[i]
        index1 = i

    elif n[i] > max2 and n[i] != max1:
        max2 = n[i]
        index2 = i

print(f"The 2nd max element is: {max2}")
print(f"Index: {index2}") """

# Question.4: Check if a list is sorted in ascending order.
""" n = [10, 20, 30, 10, 50]
is_sorted = True
for i in range(1, len(n)):
    if n[i] < n[i-1]:
        is_sorted = False
        break

if is_sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.") """

# Question.5: left Rotation by 1

""" n = [25,30,80,9,88,94,75]

for i in range(len(n)-1):
    n[i],n[i+1]= n[i+1],n[i]

print(f"the Left Rotation is: {n}.") """

# Question.6: right rotate by 1.

""" n = [25,30,80,9,88,94,75]

for i in range(len(n)-1, 0,-1):
    n[i],n[i-1]=n[i-1],n[i]

print(f"the Right Rotation is: {n}.") """

# Question.7: rev the list.

""" n = [25,30,80,9,88,94,75]

for i in range(len(n)//2):
    n[i],n[len(n)-i-1]=n[len(n)-i-1],n[i]

print(f"the rev list is: {n}.") """

# Question 8: Remove duplicates from a list

""" n = [10, 20, 30, 10, 10, 20, 50,20,20,20,20]

i = 0
while i < len(n):
    j = i + 1
    while j < len(n):
        if n[i] == n[j]:
            n.pop(j)
        else:
            j += 1
    i += 1

print(f"The list without duplicates is: {n}") """
