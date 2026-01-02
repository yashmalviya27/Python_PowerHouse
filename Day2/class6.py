# Question.1: Comparison of two numbers

""" a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater than {a}") """


# Question.2: greet the gender

""" gender = input("Enter your gender (M/F): ").strip().upper()

if gender == 'M':
    print("Hello Sir")
elif gender == 'F':
    print("Hello Ma'am")
else:
    print("Hello there") """


# Question.3: Even or Odd

""" input_number = int(input("Enter a number: "))

if input_number % 2 ==0:
    print(f"{input_number} is an Even number.")
else:
    print(f"{input_number} is an Odd number.") """


# Question.4: voting eligibility

""" age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"You are not eligible to vote. You need to wait {18 - age} more years.") """


# Question.5: day no to day name

""" day_no = int(input("Enter a day number (1-7): "))

if day_no <= 0 or day_no > 7:
    print("Invalid day number. Please enter a number between 1 and 7.")
else:
    if day_no == 1:
        print("Monday")
    elif day_no == 2:
        print("Tuesday")
    elif day_no == 3:
        print("Wednesday")
    elif day_no == 4:
        print("Thursday")
    elif day_no == 5:
        print("Friday")
    elif day_no == 6:
        print("Saturday")
    else:
        print("Sunday") """

# Question.6: gratest of three numbers

""" a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: "))

if a==b and b==c:
    print("All three numbers are equal.")
elif a==b or a==c or b==c:
    print("Two numbers are equal.")
elif a>=b and a>=c:
    print(f"{a} is the greatest number.")
elif b>=a and b>=c:
    print(f"{b} is the greatest number.")
else:
    print(f"{c} is the greatest number.") """


# Question.7: leap year or not

""" year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") """


# Question.8: shop discount calculator

""" amount = int(input("Enter the total amount: "))

if amount >= 1000 and amount <=4999:
    a = (amount*10)/100
    print(f"You got a discount of 10%.\n Final amount is {amount-a}")
elif amount>=5000:
    a = (amount*20)/100
    print(f"You got a discount of 20%.\n Final amount is {amount-a}")
else:
    print("No discount applicable.\n Final amount is", amount) """

