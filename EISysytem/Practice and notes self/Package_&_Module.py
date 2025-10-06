# =====================================
# LIBRARY, PACKAGE, AND MODULE IN PYTHON
# =====================================

'''
LIBRARY:
---------
A library in Python is a collection of useful modules and functions
that help perform specific tasks without writing code from scratch.

Examples:
- math (mathematical functions)
- random (random number generation)
- datetime (date and time handling)
- os, sys, shutil, zipfile (system operations)
- re (regular expressions)

So, a LIBRARY = COLLECTION OF PACKAGES.
'''


# PACKAGE
'''
A package is a collection of modules grouped together inside a folder.

- Every package contains a special file named __init__.py
- The __init__.py file makes Python treat the folder as a package.
- Example: 
    math → built-in package
    numpy, pandas → external packages

So, a PACKAGE = COLLECTION OF MODULES.
'''


# MODULE
'''
A module is a single Python file (.py) that contains functions, classes,
or variables which can be reused in other programs.

Example:
    - math.py (built-in)
    - random.py (built-in)
    - custom .py file created by user

So, a MODULE = COLLECTION OF FUNCTIONS / CLASSES.
'''


# =====================================
# EXAMPLES OF LIBRARY, PACKAGE & MODULE
# =====================================

# 1. Using Built-in Library (math)
import math
print("Square root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)
print("----" * 10)

# 2. Using Random Library
import random
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice([10, 20, 30, 40]))
print("----" * 10)

# 3. Using Datetime Library
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)
print("----" * 10)


# =====================================
# USER-DEFINED MODULE EXAMPLE
# =====================================
'''
To create your own module:
1. Create a new file, e.g., mymodule.py
2. Write functions in it:
       def add(a, b):
           return a + b
3. Save it in the same directory as your main file.
4. Import and use it:
       import mymodule
       print(mymodule.add(5, 10))
'''

# Example (if you had a file named mymodule.py with an add() function):
# import mymodule
# print(mymodule.add(5, 10))
