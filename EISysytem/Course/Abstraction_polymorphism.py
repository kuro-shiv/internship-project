"""
a=4
b=3

print(a+b)
print(int.__add__(a,b))
print(a-b)
print(int.__sub__(a,b))
a,b="2","4"
print(a-b)
"""
"""
class College:
    name="aaa"
    contry="India"

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,x):
        m1=self.m1+x.m1
        m2=self.m2+x.m2
        print(m1,m2)
    def __sub__(self,x):
        m1=self.m1-x.m1
        m2=self.m2-x.m2
        print(m1,m2)

s1=College(16,25)
s2=College(19,28)

s1+s2

s1-s2
"""
"""
class A:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
    def add(self,a,b,c,d):
        print(a+b+c+d)

x=A()

x.add(1,2)
"""       





















