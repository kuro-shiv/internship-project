# =====================================
# BOOLEAN 
# =====================================
print("BOOLEAN IN PYTHON")

'''
- Boolean represents one of two values: True or False
- Internally, True = 1 and False = 0
- Used for conditional statements and logical operations
'''

a = True
b = False
print("a:", a, "b:", b)
print("Type of a:", type(a))
print("Type of b:", type(b))
print()

# Logical AND
print("--" * 4 + " AND " + "--" * 4)
print("b and b:", b and b)
print("b and a:", b and a)
print("a and b:", a and b)
print("a and a:", a and a)
print("Bitwise &:", b & b, b & a, a & b, a & a)
print()

# Logical OR
print("--" * 4 + " OR " + "--" * 4)
print("b or b:", b or b)
print("b or a:", b or a)
print("a or b:", a or b)
print("a or a:", a or a)
print("Bitwise |:", b | b, b | a, a | b, a | a)
print()

# Logical XOR
print("--" * 4 + " XOR " + "--" * 4)
print("Bitwise ^:", b ^ b, b ^ a, a ^ b, a ^ a)
print()

# Logical NOT
print("--" * 4 + " NOT " + "--" * 4)
print("not a:", not a)
print("not b:", not b)
print()

# Boolean as numbers
print("True as int:", int(True))
print("False as int:", int(False))
print("1 == True:", 1 == True)
print("0 == False:", 0 == False)
print()

# Boolean conversions
print("bool(10):", bool(10))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool([1,2]):", bool([1, 2]))
print()

# Logical Operators (with variables)
'''
and  → Returns True if both are True
or   → Returns True if any one is True
not  → Inverts the boolean value
'''

x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("not y:", not y)
print()

# Logical operations with numbers
print("10 and 20:", 10 and 20)   # Returns 20 (last truthy value)
print("0 and 20:", 0 and 20)     # Returns 0 (first falsy value)
print("10 or 20:", 10 or 20)     # Returns 10 (first truthy value)
print("0 or 20:", 0 or 20)       # Returns 20 (first truthy value)
print("not 10:", not 10)
print("not 0:", not 0)
print()

# Comparison operators with booleans
print("True == 1:", True == 1)
print("False == 0:", False == 0)
print("True + True:", True + True)
print("True + False:", True + False)
print()

# Boolean expressions
print("5 > 3:", 5 > 3)
print("10 == 5:", 10 == 5)
print("7 != 2:", 7 != 2)
print("8 >= 8:", 8 >= 8)
print("3 < 1:", 3 < 1)
print()

# Truth Table Summary
print("Truth Table (Logical Operators)")
print("A\tB\tAND\tOR\tXOR")
print(f"0\t0\t{0 and 0}\t{0 or 0}\t{0 ^ 0}")
print(f"0\t1\t{0 and 1}\t{0 or 1}\t{0 ^ 1}")
print(f"1\t0\t{1 and 0}\t{1 or 0}\t{1 ^ 0}")
print(f"1\t1\t{1 and 1}\t{1 or 1}\t{1 ^ 1}")
print()

# Practice Section: Boolean with Bitwise and Binary
a, b = 20, 4
print("a =", a, "b =", b)
print("Binary of a:", bin(a))
print("Binary of b:", bin(b))

# Bitwise Operations
print("a & b (AND):", a & b, "Binary:", bin(a & b))
print("a | b (OR):", a | b, "Binary:", bin(a | b))
print("a ^ b (XOR):", a ^ b, "Binary:", bin(a ^ b))
print("~a (NOT):", ~a, "Binary:", bin(~a))
print("a << 1 (Left Shift):", a << 1, "Binary:", bin(a << 1))
print("a >> 1 (Right Shift):", a >> 1, "Binary:", bin(a >> 1))
