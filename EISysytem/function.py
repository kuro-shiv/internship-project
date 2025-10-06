# =====================================
# FUNCTION IN PYTHON
# =====================================

'''
A function is a block of reusable code used to perform a specific task.

Types:
1. Inbuilt Functions (e.g., print(), len(), type(), sum(), etc.)
2. User-defined Functions:
    - Default (Non-Parameterized)
    - Parameterized
    - Anonymous (Lambda)
'''

# -------------------------------------
# 1. Default (Non-Parameterized) Function
# -------------------------------------

def name():
    print("Hello")
    print("Bye")

def xyz():
    return "123"

def abc():
    print("456")
    return "Returned from abc()"


print("Start")
print("----" * 12)
print()

for i in range(2):
    name()

print("----" * 12)
print()

abc()
print("----" * 12)
print()

print(xyz())
print("----" * 12)
print()

print(abc())
print("----" * 12)
print()


# -------------------------------------
# 2. Parameterized Functions
# -------------------------------------

def add(a, b):   # (a, b) → formal arguments
    print("Sum =", a + b)

add(2, 7)
add(7, 9)        # (2,7) → actual arguments
print("----" * 12)
print()

# Function taking input directly inside definition
def sub(a=int(input("Enter a number: ")), b=int(input("Enter another (smaller) number: "))):
    print("Subtraction =", a - b)

sub()  # no need to pass parameters; values are input by user
print("----" * 12)
print()


# -------------------------------------
# 3. Function with Default Arguments
# -------------------------------------

def emp(name="NoName", eid=110):
    print("Name of Employee:", name)
    print("EID of Employee:", eid)

emp("Annie", 101)
emp()
emp("Allen")
print("----" * 12)
print()


# -------------------------------------
# 4. Anonymous (Lambda) Functions
# -------------------------------------
'''
Lambda function: A function without a name.
Syntax: lambda arguments : expression
'''

x = lambda a, b: a + b
print("Lambda sum:", x(3, 5))

x = lambda a, b, c: a + b * c
print("Lambda expression result:", x(3, 5, 9))

n = lambda name: print("Hello", name)
n("Ankit")
print("----" * 12)
print()


# -------------------------------------
# 5. Global and Local Variables
# -------------------------------------

a = 9   # global variable

def fun():
    global b   # declaring 'b' as global inside function
    a = 11     # local variable
    b = 50
    print("Local a:", a)
    print("Global b (declared inside function):", b)

fun()
print("Global a (outside function):", a)
print("Global b (accessible outside function):", b)
