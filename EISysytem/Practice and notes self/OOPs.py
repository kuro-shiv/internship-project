#=====================================
# OOP's - Object Oriented Programming
#=====================================

'''
OOPs is a way of programming that organizes code into objects (real-world entities)
and classes (blueprints for objects).
It makes code more modular, reusable, and easier to maintain.
'''

#===================================
# Object and Class
#===================================

'''
Object: Any real-world entity (like Car, Dog, Student)
Class: A blueprint for creating objects
'''

class Student:
    # data member / attributes
    college = "ABC University"

    # constructor
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # method
    def show(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("College:", Student.college)

# object creation
s1 = Student("Ankit", 101)
s1.show()
print("----"*12)


#==============================================
# Constructor
#==============================================

'''
Constructor: special function used to initialize objects
Automatically called when object is created
Types:
    - Default constructor: no parameters
    - Parameterized constructor: takes arguments
'''

# Default Constructor
class A:
    def __init__(self):
        print("This is a Default Constructor")

objA = A()

# Parameterized Constructor
class B:
    def __init__(self, name):
        self.name = name
        print("Parameterized Constructor called for", self.name)

objB = B("Ravi")
print("----"*12)


#===================================
# Abstraction
#===================================

'''
Hiding internal details and showing only essential features.
Example: We use the TV remote but don’t know its internal circuit.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

r = Rectangle(10, 5)
print("Area of Rectangle:", r.area())
print("----"*12)


#===================================
# Encapsulation
#===================================

'''
Wrapping of data (variables) and methods (functions) in a single unit.
We can restrict access to internal variables using private members.
'''

class Account:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a1 = Account(1000)
a1.deposit(500)
print("Current Balance:", a1.get_balance())
print("----"*12)


#===================================
# Inheritance
#===================================

'''
When one class derives (inherits) properties and behavior from another class.
Helps in code reusability.
'''

class Parent:
    def home(self):
        print("This is Parent's home.")

class Child(Parent):
    def car(self):
        print("This is Child's car.")

obj = Child()
obj.home()
obj.car()
print("----"*12)



#===================================
# Polymorphism
#===================================

'''
Polymorphism means "many forms".
Same function or operator behaving differently in different contexts.
'''

# 1. Function Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a1 = Animal()
a1.sound()

d1 = Dog()
d1.sound()
print("----"*12)

# 2. Operator Overloading
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

x = Number(5)
y = Number(7)
print("Operator Overloading Example (5 + 7):", x + y)
print("----"*12)


#===================================
# Types of Methods
#===================================

'''
There are 3 types of methods:
1. Instance Method: Works with instance variables (uses self)
2. Class Method: Works with class variables (uses cls)
3. Static Method: Independent, used for utility work
'''

class Company:
    company_name = "ANC Pvt Ltd"

    def __init__(self, ename, eid):
        self.empname = ename
        self.empid = eid

    # Instance method
    def info(self):
        print("Employee Name:", self.empname)
        print("Employee ID:", self.empid)

    # Class method
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
        print("Company name changed to:", cls.company_name)

    # Static method
    @staticmethod
    def greet():
        print("Welcome to the Company Portal!")

emp1 = Company("AAA", 111)
emp2 = Company("BBB", 222)

emp1.info()
emp2.info()
Company.greet()
Company.change_company("XYZ Pvt Ltd")
print("----"*12)
