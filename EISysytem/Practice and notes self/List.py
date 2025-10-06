# =====================================
# PYTHON LIST - COMPLETE EXPLANATION
# =====================================

print("PYTHON LISTS\n")

"""
A List in Python is:
--------------------
- An ordered collection of elements.
- Mutable (can be changed after creation).
- Can store heterogeneous data types (integers, strings, floats, complex numbers, etc.)
- Indexed (each element has a unique index starting from 0).
- Allows duplicate elements.
"""

# -------------------------------------
# List Example
# -------------------------------------
print("Example of a List:")
my_list = ["apple", 3.14, 42, True, 5 + 6j]
print("List contents:", my_list)
print("Type:", type(my_list))
print()


# -------------------------------------
# Accessing Elements and Slicing
# -------------------------------------
print("Accessing Elements and Slicing:\n")

# Access using index
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing Syntax: list[start : stop : step]
print("\nSlicing examples:")
print("my_list[1:4] →", my_list[1:4])        # elements from index 1 to 3
print("my_list[::2] →", my_list[::2])        # every 2nd element
print("my_list[::-1] →", my_list[::-1])      # reverse list
print()


# -------------------------------------
# Creating Lists in Different Ways
# -------------------------------------
print("Creating Lists using list() constructor:\n")

b = list((10, 20, 30, "python", 9.8))
print("List created using tuple:", b)
print("Type:", type(b))
print()


# -------------------------------------
# Indexing Practice
# -------------------------------------
print("Indexing examples:")
print("b[0] =", b[0])
print("b[-1] =", b[-1])
print("b[2] =", b[2])
print("b[-3] =", b[-3])
print()


# -------------------------------------
# List Slicing Practice
# -------------------------------------
print("List Slicing examples:\n")

nums = [4, 23, 6, 7, 1, 3, 5, 6, 8, 9, 61, 19, 55, 54, 911, 71]
print("Original list:", nums)
print("nums[1:-1:2] =", nums[1:-1:2])     # every 2nd element (skipping one)
print("nums[3:8] =", nums[3:8])           # elements from index 3 to 7
print("nums[-1:0:-2] =", nums[-1:0:-2])   # reverse every 2nd element
print()


# -------------------------------------
# List Methods
# -------------------------------------
print("LIST METHODS\n")

# Create a new list for method examples
a = [1, 3, 5, 7, 9]
print("Initial List:", a)
print()


# Adding Elements
print("Adding Elements: append(), insert(), extend()\n")

a.append(11)  # Adds element at the end
print("After append(11):", a)

a.insert(2, 99)  # Insert element at a specific position
print("After insert(2, 99):", a)

a.extend([100, 101, 102])  # Add multiple elements
print("After extend([100, 101, 102]):", a)
print()


# Removing Elements
print("Removing Elements: pop(), remove(), del, clear()\n")

print("Current List:", a)

a.remove(99)  # Removes the first occurrence of a specific value
print("After remove(99):", a)

a.pop(1)  # Removes element by index (index 1)
print("After pop(1):", a)

# Using 'del' to delete specific element or entire list
del a[0]
print("After del a[0]:", a)

# a.clear() empties the list but keeps it defined
a.clear()
print("After clear():", a)
print("clear() empties the list but variable still exists.\n")


# -------------------------------------
# Copy Method Demonstration
# -------------------------------------
print("COPY METHOD (copy())\n")

# Copy creates a shallow copy (new list with same elements)
original = [10, 20, 30, 40]
copy_list = original.copy()

print("Original List:", original)
print("Copied List using copy():", copy_list)

# Modify one to show independence
copy_list.append(99)
print("After appending 99 to copy_list:")
print("Original List:", original)
print("Copied List:", copy_list)
print("Note: Changes in copy_list do not affect the original list.\n")


# -------------------------------------
# More Useful List Methods
# -------------------------------------
print("More Useful List Methods:\n")

num_list = [5, 1, 3, 9, 2, 5, 3]
print("Original list:", num_list)

num_list.sort()          # Sorts in ascending order
print("After sort():", num_list)

num_list.reverse()       # Reverses the order
print("After reverse():", num_list)

print("Count of 5:", num_list.count(5))   # Count occurrences
print("Index of 9:", num_list.index(9))   # Find index position

num_list_copy = num_list.copy()            # Copies the list
print("Copied list:", num_list_copy)

# Concatenation using + operator
new_list = num_list + [100, 200, 300]
print("After concatenation:", new_list)
print()


# -------------------------------------
# Deleting Entire List
# -------------------------------------
print("Deleting the entire list using 'del':\n")
sample = [1, 2, 3]
print("Before del:", sample)
del sample
# print(sample)  # This will raise an error because 'sample' no longer exists
print("List deleted successfully.\n")


# -------------------------------------
# Other List Methods (Practice Section)
# -------------------------------------
print("OTHER LIST METHODS PRACTICE\n")

num_list = [5, 1, 3, 9, 2, 5, 3, 7, 8, 9, 4, 5, 6, 12, 2, 33, 45, 67, 89, 94, 61, 77]
print("Original List:", num_list)
print("Count of 5:", num_list.count(5))       # Count occurrences
print("Index of 94:", num_list.index(94))     # Find index position

num_list.reverse()                            # Reverse the list
print("After reverse():", num_list)

num_list.sort()                               # Sort ascending
print("After sort():", num_list)

num_list.sort(reverse=True)                   # Sort descending
print("After sort(reverse=True):", num_list)
print()


# -------------------------------------
# Summary
# -------------------------------------
print("""
Summary of Key List Methods:
---------------------------------
append()  → Add one item at end
extend()  → Add multiple items
insert()  → Insert at specific index
remove()  → Remove by value
pop()     → Remove by index
clear()   → Remove all elements
copy()    → Make a shallow copy (independent of original)
sort()    → Sort ascending
reverse() → Reverse the list
count()   → Count occurrence
index()   → Return index of first occurrence
del       → Delete list or element
---------------------------------
""")
