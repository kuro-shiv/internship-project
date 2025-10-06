# =====================================
# WHILE LOOP
# =====================================

'''
A while loop executes a block of code as long as a condition is True.

Syntax:
while condition:
    # code block

Important:
- If the condition never becomes False → Infinite loop
- Always ensure a way to update the condition (increment/decrement)
'''

# Example 1: Simple while loop
print("Example 1: Basic while loop")
i = 1
while i <= 5:
    print("i =", i)
    i += 1
print("Loop ended\n")


# Example 2: Counting down (Decrement)
print("Example 2: Countdown using while loop")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Lift off!\n")


# Example 3: Using user input
print("Example 3: User input loop")
num = int(input("Enter a number: "))
while num > 0:
    print("You entered:", num)
    num = int(input("Enter another number (0 to stop): "))
print("Loop exited\n")


# Example 4: While loop with break
print("Example 4: Using break in while loop")
n = 1
while n <= 10:
    if n == 6:
        print("Breaking at n =", n)
        break
    print("n =", n)
    n += 1
print("Loop stopped with break\n")


# Example 5: While loop with continue
print("Example 5: Using continue in while loop")
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print("Odd number:", x)
print()


# Example 6: Using pass
print("Example 6: Using pass in while loop")
y = 0
while y < 5:
    if y == 2:
        pass  # placeholder
    print("y =", y)
    y += 1
print()


# Example 7: While loop for sum of numbers
print("Example 7: Sum of first N numbers")
n = int(input("Enter N: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum =", total)
print()


# Example 8: While loop with logical operators
print("Example 8: Logical operators with while loop")
a = 1
b = 5
while a <= b and b <= 10:
    print(f"a = {a}, b = {b}")
    a += 1
    b += 1
print()


# Example 9: Infinite loop with break condition
print("Example 9: Infinite loop with exit option")
while True:
    text = input("Type 'exit' to stop: ")
    if text.lower() == "exit":
        print("Exiting loop.")
        break
    else:
        print("You typed:", text)
print()


# =====================================
# NESTED WHILE LOOP
# =====================================

# Example 10: Pattern printing
print("Example 10: Simple pattern using nested while")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
print()


# Example 11: Multiplication table using nested while
print("Example 11: Multiplication Table (1 to 5)")
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
print()
