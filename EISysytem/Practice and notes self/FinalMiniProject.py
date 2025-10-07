#=================================
# mini project
#==================================


#pwd generator
import random
s="abcdefghijklmnopqrstuvxyz"
n= int (input("Enter Lenght of password: ")) 
passwd="".join(random.choice(s) for i in range(n))
print("Your password is: ", passwd) 

#qrcode generator
import qrcode
a = qrcode.make("finallly mini project done")
a.save("final..txt")


# Speech recogination
import speech_recoginition as sr


with sr.Microphone() as s:
    print("speak now...")
    audio=r.listen(s)
    t=r.recognize_google(audio)
    print("you said: ",t)


