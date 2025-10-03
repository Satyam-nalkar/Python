# info = {
#    "key" : "value",
#    "name" : "apnacollege",
#    "subject" : ["python","c","java"],
#    "topics" : ("dictionary","set"),
#    "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4,
#     23.0 : 12
# }

# # print(type(info))
# print(info["name"])
# print(info["topics"])
# print(info["subject"])


# null_dict = {}
# null_dict["name"] = "apnacollege" 
# print(null_dict)


# info["name"] = "satyam"
# print(info)


student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 95,
        "chem" : 80,
        "math" : 90
    }
}
# nested dictionary
# print(student["subjects"]["chem"])
# print(len(student)) 
# print(list(student.keys()))
# pairs =list(student.items())
# print(pairs[0])

# print(student["name2"])  #error
# print(student.get("name2")) #no error -> None

student.update({"city" : "delhi"})
print(student)

