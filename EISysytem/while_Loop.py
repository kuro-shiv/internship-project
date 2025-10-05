# =====================================
# WHILE LOOP 
# =====================================

'''
A while loop is used to repeat a block of code
as long as a specified condition is True.

Syntax:
while condition:
    # code block

Important points:
- The condition is checked before every iteration.
- The loop continues while the condition remains True.
- If the condition becomes False, the loop stops.
- Use 'break' to exit early and 'continue' to skip one iteration.
'''

# Example 1: Simple while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # increment to avoid infinite loop
print("Loop ended\n")


# Example 2: Sum of first n natural numbers
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum of first", n, "numbers is:", total)
print()


# Example 3: Using break
i = 1
while i <= 10:
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print(i)
    i += 1
print("Loop stopped using break\n")


# Example 4: Using continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)
print("Printed only odd numbers\n")


# Example 5: Infinite loop with exit condition
while True:
    ans = input("Do you want to exit? (yes/no): ").lower()
    if ans == "yes":
        print("Exiting loop...")
        break
    print("You chose to continue.\n")
