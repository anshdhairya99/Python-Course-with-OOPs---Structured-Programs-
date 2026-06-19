# JSON MODULE IN Python :- Json- JavaScript Object Notation
# It is a data format that is used to store and exchange data between a server and a web application. It is a lightweight data format that is easy to read and write for humans and machines.   


import json

#data = '{"name": "varsh", "age": 25, "city": "New York"}'

#parsed = json.loads(data)
#print(parsed)

data2 = {
    "channel_name":"CodeWithHarry",
    "Cars":['BMW','Audi A8','Ferrari'],
    "Frideg":('roti','540')
}

jscomp =json.dumps(data2)
print(jscomp)

