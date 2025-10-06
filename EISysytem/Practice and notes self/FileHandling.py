# =====================================
# FILE HANDLING 
# =====================================

'''
File handling allows you to store, read, and modify data permanently.

MODES:
---------
"r"  → Read (default) – file must exist
"w"  → Write – creates new file or overwrites existing
"a"  → Append – adds content to end of file
"r+" → Read + Write (must exist)
"w+" → Write + Read (overwrites existing)
"a+" → Append + Read (creates if not exists)
'''

# 1️. Writing to a file
a = open("aaa.txt", "w")
a.write("Hello, I am a file.\nThis is written using write().\n")
a.close()
print("Data written successfully.\n")


# 2️. Reading from a file
b = open("aaa.txt", "r")
content = b.read()          # Reads entire file
print("File content:\n", content)
b.close()
print()


# 3️. Writing multiple lines using writelines()
a = open("aaa.txt", "w")
lines = ["Python File Handling\n", "Second line\n", "Third line\n"]
a.writelines(lines)
a.close()
print("Multiple lines written successfully.\n")


# 4️. Reading line by line
b = open("aaa.txt", "r")
print("Reading line by line:")
for line in b:
    print(line.strip())  # strip() removes \n
b.close()
print()


# 5️. Appending to an existing file
c = open("aaa.txt", "a")
c.write("This line was appended.\n")
c.close()
print("New line appended.\n")


# 6️. Using 'with' statement (auto-closes file)
with open("aaa.txt", "r") as file:
    data = file.read()
    print("Reading with 'with open':\n", data)
print("File closed automatically after 'with' block.\n")


# 7️. Reading specific parts
with open("aaa.txt", "r") as file:
    print("First 10 characters:", file.read(10))  # read first 10 chars
print()


# 8️. Checking file existence safely
import os
if os.path.exists("aaa.txt"):
    print("File exists.")
else:
    print("File not found!")
print()


# 9️. Example: Counting lines, words, and characters
with open("aaa.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Line count:", len(text.splitlines()))
    print("Word count:", len(words))
    print("Character count:", len(text))
print()


