"""
class Abc:
    name="aaa"
    age=17

    def f1(self):
        print("f1 from Abc")
    


a1=Abc()
a2=Abc()
a3=Abc()
"""
#a3.f1()

#Abc.f1()

#contructors
"""
class Company:
    name="EISystems"
    country="India"

    def __init__(self,ename,eid):
        self.empname=ename
        self.empeid=eid

    def info(self):
        print(self.empname,self.empeid)

emp1=Company("aaa",111)
emp2=Company("bbb",222)

emp2.info()
"""

class College:
    name="BIT"
    country="India"

    def __init__(self,sname,sb):                #instance method
        self.sname=sname
        self.sb=sb
    @classmethod
    def info(cls):                              #class mehtod
        print(cls.name,cls.country)
    @staticmethod
    def add(a,b):
        print(a+b)
        


s1=College("aaa","cs")
s2=College("bbb","me")

s1.add(4,5)
#College.info()
#s1.info()
#College.add(4,6)








































#print(type(a3))
#print(Abc.name,Abc.age)
#print(a1.name,a1.age)
#print(a2.name,a2.age)
#print(a3.name,a3.age)
