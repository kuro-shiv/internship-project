# =====================================
# TUPLE IN PYTHON
# =====================================
print("🔹 TUPLE 🔹")
'''
- Collection of heterogeneous data
- Ordered (indexable)
- Immutable (cannot change elements)
- Defined using ()
'''

# Tuple can hold numbers, strings, lists, etc.
a = (2, 2.5, 3+9j, [2,5,6])
print("Tuple a:", a)
print(a, type(a))

# Access elements by index
print("First element:", a[0])
print("Last element:", a[-1])

# Slicing tuple
print("Slice a[1:3]:", a[1:3])

# Length of tuple
print("Length of tuple:", len(a))

# Tuple with single element (need comma)
single = (5,)
print("Single element tuple:", single)

# Tuples are immutable
# a[0] = 10  # This will give error

# But if tuple contains a mutable element (like list), list can be modified
a[3].append(10)
print("Modified list inside tuple:", a)


# =====================================
# LIST IN PYTHON
# =====================================
print("\n🔹 LIST 🔹")
'''
- Collection of heterogeneous data
- Ordered, indexed
- Mutable (can change elements)
- Defined using []
'''

b = [1, 2, 3, 4]
print("List b:", b)

# Adding elements
b.append(5)           # Add at end
b.insert(2, 99)       # Insert at index 2
b.extend([10, 20, 30]) # Add multiple elements
print("After adding elements:", b)

# Removing elements
b.remove(99)          # Remove by value
popped = b.pop()      # Remove last element and return it
print("After removing elements:", b, "Popped:", popped)
del b[0]              # Delete by index
print("After del b[0]:", b)
b.clear()             # Empty the list
print("After clearing:", b)

# Accessing elements
c = [10,20,30,40]
print("First element:", c[0])
print("Last element:", c[-1])
print("Slice c[1:3]:", c[1:3])

# Updating elements
c[1] = 99
print("After updating:", c)

# Searching
print("Index of 30:", c.index(30))
print("Count of 99:", c.count(99))

# Copying
c_copy = c.copy()
print("Copy of c:", c_copy)


# =====================================
# BASIC OPERATIONS FOR LIST & TUPLE
# =====================================
x = [1,2,3]
y = [4,5,6]

# Concatenation
print("Concatenate x+y:", x+y)

# Repetition
print("Repeat x*2:", x*2)

# Membership
print("Is 2 in x?", 2 in x)
print("Is 10 not in x?", 10 not in x)

# Iteration
print("Iterating x:")
for i in x:
    print(i, end=" ")
print()

# Length
print("Length of x:", len(x))

# Sum, max, min (only for numeric lists)
print("Sum of x:", sum(x))
print("Max of x:", max(x))
print("Min of x:", min(x))
