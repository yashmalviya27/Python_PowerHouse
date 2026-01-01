'''now we are in string.py file'''
str1 = "Hello, World!"  # This is a string variable
str2 = 'Python is fun.'  # Another string variable
print(str1)  # Output: Hello, World!
print(str2)  # Output: Python is fun.


#string indexing and slicing
sample_str = "PowerHouse"
print(sample_str[0])  # Output: P
print(sample_str[1])  # Output: o
print(sample_str[-1])  # Output: e
print(sample_str[2:5])  # Output: wer
print(sample_str[:5])  # Output: Power
print(sample_str[5:])  # Output: House


#print statments
print("This is a print statement.")
print("Strings can be concatenated: " + str1 + " " + str2)
print(f"Using f-strings: {str1} - {str2}")
print("Using commas in print:", str1, str2)
print("Multiple arguments:", str1, str2, sample_str)
print("Escape sequences:\nNew Line\tTab\\Backslash\'Single Quote\"Double Quote")

# type conversion
num = 100
print(float(num))  # Output: 100.0
print(str(num))    # Output: "100"
print(complex(num))  # Output: (100+0j)



#input function
name = input("Enter your name: ")
print(f"Hello, {name}!")


age = int(input("Enter your age: "))
print(f"You are {age} years old.")  
height = float(input("Enter your height in meters: "))
print(f"You are {height} meters tall.") 
complex_num = complex(input("Enter a complex number (e.g., 3+4j): "))
print(f"You entered the complex number: {complex_num}")