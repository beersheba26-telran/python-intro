user: dict = {
    "name": "Vasya",
    "id": 123
}
print(f"name is {user['name']}")
print(f"id is {user.get("id")}")
# exception KeyError user["kk"] 
print (user.get("kk","default"))
user["age"] = 25
print(user["age"])
user["age"] = 26
print(user["age"])
user.update({"age":30, "address":{"city": "Lod", "street": "Sokolov"}})
print(user)
print(user.setdefault("children", 2))
print(user)
# dictionary "users"
users:dict[int,dict] = {}
#1 adding user "Vasya"
users[123] = user
#2 adding user Petya
users.setdefault(125, {"id":125, "name": "Petya"})
#3 adding user David
users.update({120:{"id": 120, "name": "David"}})
keys = [k for k in users]
print(keys)
print(users.keys())
print(users.values())
print(users.items())
print(users.popitem())
print(users)
print(users.pop(100,None))
del users[123]