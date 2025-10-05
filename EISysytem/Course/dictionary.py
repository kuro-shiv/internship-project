"""
a={
    "name":"qwerty",
    "age":12,
    "subject":["python","ML","DS"]
    }

print(a)
"""
#print(type(a))
"""
print(a.keys())
print(a.values())
print(a.items())

#a.pop("name")
#a.popitem()
#a.clear()
del a["name"]
print(a)

a["country"]="India"
a["phone"]=12345
a["age"]=35
print(a)
"""
#print(a[0])
"""
print("start")
#print(a["country"])
print(a.get("age","not found"))
print("stop")

print(a["name"])
print(a["age"])
print(a["subject"])
print("----------------------------")
print(a.get("name"))
"""
"""
a={
    "name":"aaa",
    "age":11
    }

b=a.copy()
print(a,id(a),": a")
print(b,id(b),": b")
print("-----------------------")
a["school"]="BIT"
print(a,id(a),": a")
print(b,id(b),": b")

"""


"""
a={
    "name":"aaa",
    "age":11
    }

print(a)
a["phone"]=12345
print(a)

a.update({
    "name":"bbb",
    "college":"qwerty",
    "state":"Maharastra"
    })
print(a)

"""

"""
company={
    "e1":{
        "name":"aaa",
        "eid":112
        },
    "e2":{
        "name":"bbb",
        "eid":116
        }
    }
print(company)
print(type(company))
print(company["e1"]["name"])
print(company.get("e2")["eid"])
print(company.get("e2").get("eid"))

"""
e1={
    "name":"aaa",
    "eid":112
    }
e2={
    "name":"bbb",
    "eid":116
    }
print(e1)
print(e2)

e={
    1:e1,
    2:e2
    }
print(e)
print(e[2]["name"])


















"""
a=dict(name="aaa",age=12)
print(a,type(a))
"""






















































