# while loop example
""" n =int(input("Enter the number: "))
i =0
while i <= n:
    print(f"{i} hello")
    i += 1 """


# Question.1: Print each digit in reverse order

""" n = int(input("enter the num: "))
ans = 0
while n>0:
    digit = (n%10)
    ans = ans*10+digit
    n = n//10

print(f"result is {ans}") """

# Question.2: sum of digits of a number

""" n = int(input("Enter the digit you want to sum: "))

ans = 0
while n>0:
    digit = n%10
    ans+=digit
    n=n//10

print(f"ans is: {ans}") """

# Question.3: rev the num 

""" n = int(input("enter the num: "))
ans = 0
while n>0:
    digit = (n%10)
    ans = ans*10+digit
    n = n//10

print(f"result is {ans}") """

# Question.4: check the num is palindrome or not 

""" n= int(input("Enter the no to check the number is Pailindrom or not: "))

check = n
ans = 0

while n>0:
    digit = n%10
    ans = (ans*10)+digit
    n = n//10

if check==ans:
    print(f"the given is Pailindrom {ans}:{check}")
else:
    print(f"The given no is not Pailindrom {ans}:{check}") """

# Question.5: automorphic number

n = int(input("Enter the number you want to find an automorphic no ot not: "))
copy = n
count = 0
ans = n**2

while n>0:
    count+=1
    n = n//10

ans = ans%(10**count)
if copy==ans:
    print(f"{copy} is an automorphic num.")
else:
    print("Not an automorphic num.")