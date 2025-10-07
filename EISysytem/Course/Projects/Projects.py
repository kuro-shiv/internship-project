"""
for i in range(5):
    for j in range(5):
        if (i==0 or i==4 or j==0 or j==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
"""
for i in range(7):
    for j in range(5):
        if (i==3 or j==0 or j==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
"""
for i in range(7):
    for j in range(4):
        if (i==0 or i==3 or j==0 or ((i==1 or i==2)and j==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
"""
for i in range(7):
    for j in range(4):
        if (i==0 or i==3 or j==0 or (j==3 and i<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

"""
"""
for i in range(7):
    for j in range(4):
        if (j==0 or (j==3 and (i>0 and i<3)) or (i==0 or i==3)and j!=3):
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
"""
import random
import string
s=string.ascii_letters+string.digits+string.punctuation
print(s)
n=int(input("enter the length of passwd : "))

passwd="".join(random.choice(s) for i in range(n))
print("your passswd is : ",passwd)
"""
#QRCODE
import qrcode
#a=qrcode.make("https://www.google.com/")
#a.save("myqrcode.png")

#a=qrcode.make("https://drive.google.com/file/d/1w2-fmVBzXLFFSsvaVNiH09gQcrHtLDpF/view?usp=sharing")
#a.save("image.png")


#speech recognition
"""
import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as s:
    print("speak now...")
    audio=r.listen(s)
    t=r.recognize_google(audio)
    print("you said : ",t)
"""

















































































































