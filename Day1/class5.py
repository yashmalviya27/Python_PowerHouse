#comparison operators
a=15
b=20
print(a==b) #equal to
print(a!=b) #not equal to   
print(a>b) #greater than
print(a<b) #less than    
print(a>=b) #greater than or equal to
print(a<=b ,"\n") #less than or equal to  

#logical operators
x=True
y=False 
print(x and y) #logical and
print(x or y)  #logical or  
print(not x , "\n")    #logical not 


#membership operators
str1="Hello World"  
print("Hello" in str1)  #membership operator
print("Python" not in str1 , "\n") #membership operator


#identity operators
a=10
b=10
print(a is b) #identity operator
print(a is not b , "\n") #identity operator


#bitwise operators
a=5  #binary: 0101
b=3  #binary: 0011  
print(a & b) #bitwise and
print(a | b) #bitwise or    
print(a ^ b) #bitwise xor
print(~a)    #bitwise not    
print(a << 2) #bitwise left shift
print(a >> 2) #bitwise right shift      
