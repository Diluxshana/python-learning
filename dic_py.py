# creating dictionary
info = {'name': "dilux", "age": 31, "city": "srilanka"}
print(info["name"])
print(info)
print(info.get("name"))

info["name"] = "shana"
print(info)
#info.update("age": 31, 'name': "diluxshana")
# print(info)
del info["age"]
print(info)
age = info.pop("age", 0)

#loop
for i in range (5):
    print(i)

names=["dilux","shana","mathu","sar","rusan"]
for name in names:
    print(name)
