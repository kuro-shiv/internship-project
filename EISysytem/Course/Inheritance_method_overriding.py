#Single level inheritance
"""
class A:
    def f1(self):
        print("f1 from A")
    def f2(self):
        print("f2 from A")

class B(A):
    def f3(self):
        print("f3 from B")
a=A()
b=B()

a.f1()
a.f2()
b.f3()
b.f1()    
b.f2()  
a.f3()
"""

#Multilevel inheritance
"""
class A:
    def f1(self):
        print("f1 from A")
    def f2(self):
        print("f2 from A")

class B(A):
    def f3(self):
        print("f3 from B")

class C(B):
    def f4(self):
        print("f4 from C")
a=A()
b=B()
c=C()

b.f1()
b.f2()
c.f1()
c.f2()
c.f3()
"""
#hierarchical inheritance

"""
class A:
    def f1(self):
        print("f1 from A")
    def f2(self):
        print("f2 from A")

class B(A):
    def f3(self):
        print("f3 from B")

class C(A):
    def f4(self):
        print("f4 from C")
a=A()
b=B()
c=C()

b.f1()
b.f2()
b.f3()
c.f1()
c.f2()
c.f4()
"""


#Multiple
"""
class A:
    def f1(self):
        print("f1 from A")
    def f2(self):
        print("f2 from A")

class B:
    def f3(self):
        print("f3 from B")

class C(A,B):
    def f4(self):
        print("f4 from C")
a=A()
b=B()
c=C()

c.f1()
c.f2()
c.f3()
c.f4()
"""

#Hybrid
"""
class A:
    def f1(self):
        print("f1 from A")
    def f2(self):
        print("f2 from A")

class B:
    def f3(self):
        print("f3 from B")

class C(A,B):
    def f4(self):
        print("f4 from C")
class D(C):
    def f5(self):
        print("f5 from D")

class E(C):
    def f6(self):
        print("f4 from E")
a=A()
b=B()
c=C()
d=D()
e=E()

c.f1()
c.f2()
c.f3()
c.f4()
d.f1()
d.f2()
d.f3()
d.f4()
d.f5()
e.f1()
e.f2()
e.f3()
e.f4()
e.f6()
"""


class A:
    def f1(self):
        print("f1 from A")

class B(A):
    def f1(self):
        print("f1 from B")
        super().f1()
    def f2(self):
        print("f2 from B")
a=A()
b=B()

#a.f1()
#b.f2()
b.f1()







































































