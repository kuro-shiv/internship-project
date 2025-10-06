# =====================================
# FOR LOOP 
# =====================================

'''
The for loop is used to iterate (loop) over a sequence such as:
- list
- tuple
- string
- dictionary
- range()

Syntax:
for variable in sequence:
    # code block
'''

# Example 1: Loop through a range of numbers
print("Example 1: Simple range loop")
for i in range(5):
    print("i =", i)
print("Loop ended\n")


# Example 2: Loop with range(start, stop, step)
print("Example 2: Range with step")
for i in range(1, 11, 2):
    print(i)
print()


# Example 3: Loop through a list
print("Example 3: Looping through a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
print()


# Example 4: Loop through a string
print("Example 4: Loop through string")
name = "Python"
for ch in name:
    print(ch)
print()


# Example 5: Loop through a dictionary
print("Example 5: Loop through dictionary")
student = {"name": "Shivam", "age": 21, "course": "Python"}
for key, value in student.items():
    print(key, ":", value)
print()


# Example 6: Using range for basic arithmetic operation
print("Example 6: Square of numbers 1 to 5")
for i in range(1, 6):
    print(f"{i}² =", i**2)
print()


# Example 7: Using break
print("Example 7: Using break")
for i in range(1, 10):
    if i == 5:
        print("Breaking at i =", i)
        break
    print(i)
print("Loop ended with break\n")


# Example 8: Using continue
print("Example 8: Using continue")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)
print()


# Example 9: Using pass
print("Example 9: Using pass")
for i in range(5):
    if i == 3:
        pass  # placeholder for future logic
    print("i =", i)
print()


# =====================================
# NESTED FOR LOOP
# =====================================

# Example 10: Nested for loop - pattern printing
print("Example 10: Printing a simple pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # new line
print()


# Example 11: Multiplication table using nested loops
print("Example 11: Multiplication Table (1 to 5)")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
print()


# Example 12: Nested loop - sum of matrix elements
print("Example 12: Matrix sum using nested loop")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for row in matrix:
    for num in row:
        total += num
print("Sum of all matrix elements:", total)
print()
