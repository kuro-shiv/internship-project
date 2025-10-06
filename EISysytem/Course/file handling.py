"""
a=open("aaa.txt","w")
a.write("hello  I am a file")
a.close()
"""
"""
a=open("aaa.txt","r")
print(a.read())
"""
"""
a=open("aaa.txt","a")
a.write(" i am appended")
a.close()
"""

#open("qwerty.xlsx","w")
"""
x=open("aaa.txt","a")
x.write("hiiii")
x.close()
"""


#import os

#os.rename("aaa.txt","bbb.txt")
#os.remove("qwerty.pdf")
#os.mkdir("hello123")
#os.rmdir("hello123")

import shutil
#shutil.copy("bbb.txt","D:\\New folder")
#shutil.move("qwerty.xlsx",r"D:\New folder")

import os.path

#if os.path.isfile(r"C:\Users\91798\OneDrive\Desktop\projects1.py"):
#    print("file found")
#else:
#    print("file not found")

#if os.path.isdir(r"C:\Users\91798\OneDrive\Desktop\Data Files111"):
#    print("folder found")
#else:
#    print("folder not found")

#if os.path.exists(r"C:\Users\91798\OneDrive\Desktop\Data Files"):
#    print("file found")
#else:
 #   print("file not found")


import zipfile
"""
x=zipfile.ZipFile("myzipfile.zip","w")
x.write("bbb.txt")
x.write("qwerty.mp4")
x.close()

"""

#a=zipfile.ZipFile("myzipfile.zip")
#a.extractall(r"D:\New folder\Python")


a1=[1,2,3,4,5]
a2=[6,7,8,9,10]

z=list(zip(a1,a2))
print(z)

for i,j in z:
    print(i+j)






































