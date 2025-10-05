# =====================================
# CONTROL STATEMENTS
# =====================================

# 1️Single if statement - Example 1
a = int(input("Enter a number: "))
if a == 10:
    print("You entered 10")
print("Done Example 1\n")

# Single if statement - Example 2
b = int(input("Enter a number: "))
if b % 2 == 0:
    print("Even number")
print("Done Example 2\n")


# 2️if-else statement - Example 1
x = int(input("Enter a number: "))
if x > 0:
    print("Positive number")
else:
    print("Non-positive number")
print()

# if-else statement - Example 2
y = int(input("Enter a number: "))
if y % 2 == 0:
    print("Even")
else:
    print("Odd")
print()


# 3️if-elif-else statement - Example 1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
print()

# if-elif-else statement - Example 2
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade F")
print()


# 4️Comparing two numbers - Example 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First is greater")
elif a == b:
    print("Both are equal")
else:
    print("Second is greater")
print()

# Comparing two numbers - Example 2
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
if p % q == 0:
    print("First is divisible by Second")
else:
    print("Not divisible")
print()


# 5️Nested if statement - Example 1
n = int(input("Enter a number for nested if: "))
if n > 0:
    print("Positive")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif n == 0:
    print("Zero")
else:
    print("Negative")
print()

# Nested if statement - Example 2
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Young Adult")
else:
    print("Minor")
print()


# 6️Logical Operators - Example 1 (and, or)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > 0 and b > 0:
    print("Both numbers are positive")
if a > 0 or b > 0:
    print("At least one number is positive")
print()

# Logical Operators - Example 2 (not)
c = int(input("Enter a number: "))
if not c > 0:
    print("Number is zero or negative")
else:
    print("Number is positive")
print()


# 7️⃣ Comparing three numbers with logical operators - Example 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("a is greater than b and c")
elif b > a and b > c:
    print("b is greater than a and c")
else:
    print("c is greatest")
print()

# Comparing three numbers with logical operators - Example 2
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x >= y or x >= z:
    print("x is greater than or equal to y or z")
if not (y > z):
    print("y is not greater than z")
