#if else statements

age = int(input("Enter your age: "))

#in ths : <---- this is indentation of <= we use <

if age<18:
    print("You are a minor.")
elif age==18:
    print("You are just an adult.")
else:
    print("You are an adult.")


#tarinary if else
num = int(input("Enter a number: "))
result = "positive" if num > 0 else "zero" if num == 0 else "negative"
print(f"The number is {result}.")

print("\n")
#nested if else
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")


# indentation is very important in python as it defines the block of code
#5 spaces or 1 tab is used for indentation in python
else:
    print("The number is negative.")

#pass is used to avoid error in empty if else statements
num = int(input("Enter a number: "))
if num > 0:
    pass  # TODO: implement positive number handling    
else:
    print("The number is not positive.")



print("\n")
