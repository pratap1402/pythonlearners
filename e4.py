# students dictionary
students={
    "s1":{
        "name":"John",
        "age":28,
        "married":True,
        "pets":None,
        "children":("abc","def"),
        "cars": [{"model": "m11", "mpg": 10},
                {"model": "m12", "mpg": 16}],
        "marks":{"physics":70,"Maths":71,"chemistry":72}},
    "s2": {
        "name": "Mike",
        "age": 26,
        "married": True,
        "pets": None,
        "children": None,
        "cars": [{"model": "m21", "mpg": 12},
                 {"model": "m22", "mpg": 16}],
        "marks": {"physics": 97, "Maths": 84, "chemistry": 85}},
    "s3": {
        "name": "mac",
        "age": 27,
        "married": False,
        "pets": None,
        "children": None,
        "cars": [{"model": "m31", "mpg": 17},
                 {"model": "m32", "mpg": 13}],
        "marks": {"physics": 100, "Maths": 94, "chemistry": 95}},
}

#questions and implementation
# 1. names of students with age > 25
# names = []
# for key,value in students.items():
#     for k1,v1 in value.items():
#         if k1 == "age" and v1 > 25:
#             names.append(value["name"])
# print(names)

# 2. name of student with highest marks in physics
# name = ''
# highest = 0
# for key,value in students.items():
#     # print(f"key:{key}, value:{value}")
#     for k1,v1 in value.items():
#         # print(f"key:{k1}, value:{v1}")
#         if k1 == "marks" and v1["physics"] > highest:
#             highest = v1["physics"]
#             name = value["name"]
# print(name)

# 3. car models of student with no children
# cars = []
# for key,value in students.items():
#     for k1,v1 in value.items():
#         if k1 == "children" and v1 is None:
#             for ele in value["cars"]:
#                 cars.append(ele["model"])
# print(cars)
