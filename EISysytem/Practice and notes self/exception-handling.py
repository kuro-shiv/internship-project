# =====================================
# EXCEPTION HANDLING 
# =====================================

'''
EXCEPTION:
-----------
An Exception is an error that occurs during the execution of a program
(disrupting its normal flow).

ERROR TYPES:
-------------
1. Syntax Error / Compile-Time Error  → Detected before execution.
   Example: print("Hello"   → Missing parenthesis

2. Logical Error  → Program runs but gives wrong output.
   Example: average = total / 0   (wrong logic)

3. Runtime Error / Exception  → Error during execution.
   Example: dividing by zero, opening a missing file, wrong input, etc.

Exception handling allows the program to continue running instead of crashing.
'''

# =====================================
# EXAMPLE 1: BASIC try-except
# =====================================

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)

except:
    print("An error occurred (maybe division by zero or invalid input).")

print("Program continues...\n")


# =====================================
# EXAMPLE 2: SPECIFIC EXCEPTIONS
# =====================================

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Division:", x / y)

except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter numbers only.")
except Exception as e:
    print("Some other error occurred:", e)

print("After handling specific exceptions.\n")


# =====================================
# EXAMPLE 3: try - except - else - finally
# =====================================

try:
    num = int(input("Enter a number to check even/odd: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
finally:
    print("This block always executes (cleanup or closing files).\n")


# =====================================
# EXAMPLE 4: RAISING EXCEPTIONS MANUALLY
# =====================================

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise Exception("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("Exception:", e)
print()


# =====================================
# EXAMPLE 5: USING 'pass' AND 'finally'
# =====================================

try:
    num = int(input("Enter a number: "))
    print("10 divided by number =", 10 / num)
except ZeroDivisionError:
    pass  # simply ignore the exception
finally:
    print("Finally block executed even if exception occurred.")

print("End of program.\n")
