# =====================================
# DICTIONARY
# =====================================
print("DICTIONARY \n")

# 1️Creating dictionaries
dict1 = {}  # Empty dictionary
dict2 = {"name": "Alice", "age": 25, "city": "London"}  # Pre-filled dictionary
print("dict2:", dict2)

# 2️Accessing elements
print("Access by key 'name':", dict2["name"])       # Using key
print("Access using get():", dict2.get("age"))     # Using get() - safer
print("Access non-existing key with get():", dict2.get("country", "Not Found"))

# 3️Adding / Updating elements
dict2["country"] = "UK"            # Add new key
dict2["age"] = 26                   # Update existing key
dict2.update({"name": "Bob", "profession": "Engineer"})  # Update multiple keys
print("After adding/updating:", dict2)

# 4️Removing elements
val = dict2.pop("city")            # Remove key and get value
print("Removed 'city':", val)
last_item = dict2.popitem()        # Remove last inserted key-value pair
print("Removed last item:", last_item)
del dict2["profession"]             # Delete key permanently
print("After deletion:", dict2)

# 5️Checking membership
print("'name' in dict2?", 'name' in dict2)
print("'city' not in dict2?", 'city' not in dict2)

# 6️Iterating dictionaries
print("\nIterating keys:")
for key in dict2:
    print(key, end=", ")
print("\nIterating values:")
for value in dict2.values():
    print(value, end=", ")
print("\nIterating items (key-value pairs):")
for key, value in dict2.items():
    print(f"{key}: {value}")

# 7️Dictionary methods for retrieving data
print("\nKeys:", dict2.keys())
print("Values:", dict2.values())
print("Items:", dict2.items())

# 8️Copying dictionaries
dict_copy = dict2.copy()  # Shallow copy
print("Original:", dict2)
print("Copy:", dict_copy)

# 9️Clearing a dictionary
dict2.clear()
print("After clearing:", dict2)

# 10 Nested dictionaries
nested = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print("Nested dictionary:", nested)
print("Access nested value:", nested["student1"]["name"])

# 11 Dictionary comprehension
squares = {x: x*x for x in range(5)}
print("Dictionary comprehension (squares):", squares)

# 12 Merging dictionaries (Python 3.9+)
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
merged = dict_a | dict_b  # b from dict_b overrides dict_a
print("Merged dictionary:", merged)

# 13 Other useful methods
sample = {"x": 10, "y": 20}
print("get():", sample.get("x"))
print("setdefault():", sample.setdefault("z", 30))  # Adds key if not exists
print("After setdefault():", sample)

# 14 Length of dictionary
print("Length of sample dictionary:", len(sample))
