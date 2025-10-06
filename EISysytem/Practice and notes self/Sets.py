# =====================================
# SET 
# =====================================
print("SET IN PYTHON")

'''
- Collection of unique elements
- Unordered (no indexing, no slicing)
- Mutable (can add/remove elements)
- Elements must be immutable (numbers, strings, tuples)
- Defined using {} or set()
'''

# 1. Creating sets
s1 = {1, 2, 3, 4, 4, 2}  # Duplicates automatically removed
s2 = set([3, 4, 5, 6])
s3 = set()  # Empty set (use set(), {} creates a dict)

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

print("s1:", s1)
print("s2:", s2)
print("Empty set:", s3)

# 2. Accessing elements
# No indexing or slicing
# Use loops or membership test
print("Is 3 in s1?", 3 in s1)
print("Is 10 not in s1?", 10 not in s1)

# 3. Adding elements
s1.add(10)              # Add single element
s1.update([11, 12, 13]) # Add multiple elements
print("After adding elements:", s1)

# 4. Removing elements
s1.remove(2)            # Removes element, raises KeyError if not found
s1.discard(100)         # Removes element, does NOT raise error
popped = s1.pop()       # Removes and returns a random element
print("After removing elements:", s1)
print("Popped element:", popped)

# 5. Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a | b (Union):", a | b)
print("Union using method:", a.union(b))
print("a & b (Intersection):", a & b)
print("Intersection using method:", a.intersection(b))
print("a - b (Difference):", a - b)
print("Difference using method:", a.difference(b))
print("a ^ b (Symmetric Difference):", a ^ b)
print("Symmetric Difference using method:", a.symmetric_difference(b))

# 6. Iterating
print("Iterating set a:")
for i in a:
    print(i, end=", ")
print("\n")

# 7. Copy and Clear (Memory behavior)
s = {1, 2, 3}
z = s  # Both point to same object (alias)
s1_copy = s1.copy()  # Creates a shallow copy (different object)

print(s, id(s), "s")
print(z, id(z), "z")
print(s1_copy, id(s1_copy), "s1_copy")

s.clear()  # Removes all elements
print("After clear:", s)
print("z after s.clear():", z)  # z also gets cleared (same reference)
print("Copied set remains:", s1_copy)

# If we want independent sets:
s = {1, 2, 3}
z = s.copy()
print("\nIndependent copy check:")
print(s, id(s))
print(z, id(z))
s.add(100)
print("After modifying s:", s)
print("z remains unchanged:", z)

# 8. Set Update Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.difference_update(b)  # Removes elements found in b
print("After difference_update:", a)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.update(b)  # Union update (adds all elements)
print("After update (union_update equivalent):", a)
