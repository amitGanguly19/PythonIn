# Numercal operatos in Python

# + for addition
# - for substractions 
# * for multiplication
# / for float division
#// for integer division
# ** for power calculation
# % for modulus 

x = 5
y = 3 

print("Addition of x + y = ", x + y)
print("Substraction of x - y = ", x - y)
print("Multipliccation of x * y = ", x * y)
print("float Division of x / y = ", x / y)
print("integer division of x // y = ", x // y)
print("Modulus of x % y = ", x % y)
print("Power of y on x = ", x ** y)

# some operations on string

str_data = "Amit"
empty_str = ""

# concat operation for string    #It will work as it is defined
full_name = str_data + " "  + "Ganguly"
print("Full name = ", full_name)

Multi_str = "Amit " * 3 #this work as its predefine 
print("multi = ", Multi_str)
print(type(Multi_str))

# if we can use - as well ? It will not work as its not defined
# minur_str = "amit" - "Ganguly"
# print("Minus str = ", minur_str)

# Multipy_str = "Amit" * "Ganguly"     it will not work as its not defined
# print("Multiply = ", Multipy_str)

# power_str = "amit" ** "Ganguly"      it will not work as its not defined
# print("Power = " , power_str)

# Assignment Operators
# = , x = 5
# +=, x +=  5 -> x = x + 5
# -=, x -= 5 -> x = x - 5
# *=, x *= 5 -> x = x * 5
# /=, x /= 5 -> x = x / 5
# //=, x //= 5 -> x = x // 5
# %=, x %= 5 -> x = x % 5


# Comparison operators 
# == , Equals to condition, x == y
# != , Equals to condition, x != y
# > , Equals to condition, x > y
# < , Equals to condition, x < y
# >= , Equals to condition, x >= y
# <= , Equals to condition, x <= y

a = 10 
b = 5
print("Result of a == b ", a == b)
print("Result of a != b ", a != b)
print("Result of a > b ", a > b)
print("Result of a < b ", a < b)
print("Result of a >= b ", a >= b)
print("Result of a <= b ", a <= b)

# Logical Operators in Python (logical check will happen for expression result)
# and -> Returns true both statement are true
# or -> Returns true if one of the statements are true
# not-> reverse the result, returns false if the result is true

m =10
n= 8
print("m>10 and n<10, Result = ", m>10 and n<10)
print("m>10 or n<10, Result = ", m>10 or n<10)
print("not(m>10 and n<10), Result = ", not(m>10 and n<10))
