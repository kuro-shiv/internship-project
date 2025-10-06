# =====================================
# FILE HANDLING 2
# =====================================

# 1. Creating and writing to a file
file = open("test.pdf", "w")   # creates a new file (or overwrites if it exists)
file.write("This is a PDF test file.")
file.close()

# 2. Appending text to an existing file
x = open("aaa.txt", "a")   # 'a' = append mode
x.write("Hi, this is appended text.\n")
x.close()

# 3. Reading from a file
r = open("aaa.txt", "r")
print("File content:")
print(r.read())
r.close()

# 4. Renaming a file
import os
if os.path.exists("aaa.txt"):
    os.rename("aaa.txt", "bbb.txt")
    print("File renamed successfully.")
else:
    print("File not found for renaming.")

# 5. Copying and moving files
import shutil
# Copy file
shutil.copy("bbb.txt", "copy_bbb.txt")    # creates a duplicate
# Move file (renames or changes location)
shutil.move("copy_bbb.txt", "moved_bbb.txt")

# 6. Deleting files
if os.path.exists("bbb.txt"):
    os.remove("bbb.txt")
    print("File deleted.")
else:
    print("File not found for deletion.")

# 7. Creating and deleting folders
if not os.path.exists("sample_folder"):
    os.mkdir("sample_folder")
    print("Folder created.")

if os.path.exists("sample_folder"):
    os.rmdir("sample_folder")
    print("Empty folder deleted.")

# 8. Creating and extracting ZIP files
import zipfile

# Create a ZIP file
with zipfile.ZipFile("archive.zip", "w") as zipf:
    zipf.write("moved_bbb.txt")
    print("File added to zip.")

# Extract ZIP file contents
with zipfile.ZipFile("archive.zip", "r") as zipf:
    zipf.extractall("extracted_files")
    print("Zip extracted into 'extracted_files' folder.")


a1 =[1,2,3,4]
a2 =[5,6,7,8,9,10]
z=list(zip(a1,a2))
print(z)


for i,j in z:
    print(i,j)
