# =====================================
# NESTED DICTIONARY EXAMPLES
# =====================================

# Nested dictionary
company = {
    "e1": {
        "name": "devi",
        "age": 21,
        "eid": 310
    },
    "e2": {
        "name": "meghana",
        "age": 21,
        "eid": 551
    }
}

print("Company dictionary:", company)
print("Type:", type(company))

# Accessing nested values
print("Name of e1:", company["e1"]["name"])
print("EID of e2:", company["e2"]["eid"])
print("Using get():", company.get("e2").get("eid"))
print("Whole e2 entry:", company.get("e2"))

# Deleting the entire dictionary
del company
print("Company deleted")
print("----"*12)

# Creating separate employee dictionaries
empx = {"name": "devi", "age": 21, "eid": 310}
empy = {"name": "meghana", "age": 21, "eid": 551}

print("Employee X:", empx)
print("Employee Y:", empy)

# Creating a dictionary of employees
employees = {
    1: empx,
    2: empy
}
print("Employees dictionary:", employees)

# Deleting individual employee dictionaries
del empx
del empy
print("Deleted empx and empy")
print("----"*12)

# Creating a dictionary using dict() constructor
a = dict(name="aaa", age=12)
print("Dictionary using dict():", a)
print("Type:", type(a))
