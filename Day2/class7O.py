# Question.1: Print "hello" n time

""" n = int(input("Enter Number: "))

for i in range(n):
    print("hello") """

# Question.2: Print numbrt 1 to n

""" n = int(input("enter the num: "))

for i in range(n):
    print(i+1) """

# Question.3: sum of natural number n to 1

""" n = int(input("Enter a number: "))

for i in range(n , 0 ,-1):
    print(i) """

# Question.4: sum of natural number 1 to n

""" n = int(input("Enter a number: "))
sum = 0
for i in range(n):
    sum = sum + (i+1)
print(sum) """

# Question.5: Print factorial of a number

""" n = int(input("Enter the number: "))

fac = 1 
for i in range(1,n+1,1):
    fac*= (i)
print(fac) """

# Question.6: sum of all even and sum of all odd num 

""" n = int(input("Enter the num: "))

sum_odd = 0
sum_even = 0

for i in range(n+1):
    if (i%2)==0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of even numbers is {sum_even} \nSum of odd numbers is {sum_odd}") """

# Question.7: Print all the factors of the "n" number

""" n = int(input("ente the number: "))

for i in range(1,n+1,1):
    if (n%i)==0:
        print(i) """
    
# Question.8: Print all the factors of the "n" number

""" n = int(input("ente the number: "))
sum = 0
for i in range(1,n+1,1):
    if (n%i)==0:
        sum+=i
print(sum) """    

# Question.9: 