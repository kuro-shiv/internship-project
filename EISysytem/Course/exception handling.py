"""
print("start")

a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
x=[2,7,4,5]

try:
    print(a/b)
    print(x[3])
    eid=int(input("enter the eid of the employee : "))
    print("eid of the employee is : ",eid)

except ZeroDivisionError:
    print("can't divide any number with zero")
except IndexError:
    print("Index out of range")
#except Exception:
#    print("something went wrong")
finally:
    print("end")
"""

x=int(input("enter the value of x : "))
if x>10:
    print(x)
else:
    raise ValueError("value of x is not greater than 10")




















