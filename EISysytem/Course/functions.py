"""
def Myname():
    print("Hello")
    print("My name is Mallika")
    print("Bye")

print("out of the function")

for i in range(5):
    Myname()
"""
"""
def abc():
    print("hello")

abc()

def xyz():
    return "123"
print(print(print(xyz())))
"""
"""
def add(a,b):
    print(a+b)

add(2,7)
add(5,9)
"""
"""
def add(a=int(input("enter the value for a ")),b=int(input("enter the value for a "))):
    print(a+b)

add()

"""

"""
def add(a,b):
    return a+b,a-b,a*b,a/b


print(add(3,4))

"""
"""
def emp(name="hello",eid=112):
    print("name of the employee is : ",name)
    print("eid of the employee is : ",eid)

"""

#emp("qwerty",112)
#emp("xyz",890)
#emp("qwertyy")
#emp(223,"xyz")
#emp("apple",117)
"""
t=lambda a,b:a+b
print(t(5,6))

x=lambda a,b,c:a*b*c
print(x(2,7,3))

"""
"""
n=lambda name:print("Mallika")
n(1)
"""



a=9
b=20
c=30
def f1():
    #global a
    a=100
    print("local : ",a)
    g=globals()
    print("global var : ",g.get("a"))


f1()
print("outside : ",a)























































































