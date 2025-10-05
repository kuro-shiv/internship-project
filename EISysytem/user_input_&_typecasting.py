# =====================================
# USER INPUT & TYPECASTING
# =====================================
print("USER INPUT & TYPECASTING IN PYTHON\n")

# Example 1: Basic addition
a = 2
b = 4
c = a + b
print("a + b =", c)

# Example 2: Taking string input
variable = input("Enter something: ")
name = input("Enter your name: ")
print("Hello,", name)

# Example 3: Input needs typecasting
num = int(input("Enter a number: "))  # Convert input to integer
print("Number + 10 =", num + 10)

# Example 4: Sum of two numbers from user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# Example 5: Price * Quantity
x = float(input("Enter price: "))
y = int(input("Enter quantity: "))
total = x * y
print("Total =", total)

# Example 6: Typecasting between data types
a = 10
b = 10.7
c = "15"
d = True

print("\nTypecasting examples:")
print("float(a):", float(a))   # 10.0
print("int(b):", int(b))       # 10
print("int(c):", int(c))       # 15
print("str(d):", str(d))       # "True"
print("bool(0):", bool(0))     # False
print("bool(5):", bool(5))     # True

# Example 7: Multiple user inputs and calculations
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

print("\nUser Information:")
print("Name:", name)
print("Age in 5 years:", age + 5)
print("Height:", height, "m")
