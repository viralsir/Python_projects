'''
   dicttionary : { key:value , key:value,----}
   json
   <name>value</name>
   <key>value</key>

   data - sharing

   <email>viralsir2018</email>
   <password>232323</password>

   .xml
   <authenticated>True</authenticated>  webservice

   json // dictionary

   {
      email: 'viralsir2018',
      password: '232323',
   }

   sql    --> table
   nosql --> json
     {}  -> operation
'''
# dict={1:"first","second":3,4:3433.343}
# #item -> key:value
# print(dict)
# print(dict[1])
# print(dict["second"])
#
# dict[1]="one"
# print(dict)
# dict["five"]=3434343.3434
# print(dict)
# print("=== only keys ====")
# for key in dict.keys():
#     print(key)
# print("=== only values ====")
# for value in dict.values():
#     print(value)
# print("== key and value ====")
# for key,value in dict.items():
#     print(key,value)
#
# if "first" in dict :
#     print("first found in key")
# else :
#     print("first not found in key")
#

# person={"name":"vimal","age":23,"city":"Ahmedabad","phonenumber": {"office":"+919812312345","home":"+9176123123455"}}
# print(person)
# print(person["name"])
# print(person["age"])
# print(person["city"])
# print(person["phonenumber"]["office"])
# print(person["phonenumber"]["home"])



students=[
    {"name":"amit","maths":23,"science":33,"english":34},
    {"name":"rajan","maths":43,"science":33,"english":34},
    {"name": "raj", "maths": 43, "science": 33, "english": 34},
    {"name": "ajan", "maths": 43, "science": 33, "english": 34}
]
div={"A":students,"B":[{"name":"amit","maths":23,"science":33,"english":34},
    {"name":"rajan","maths":43,"science":33,"english":34}]}
print(students[0])
print(students[0]["name"])
print(students[1]["name"])

for student in students:
    for key,value in student.items():
        print(key,value)
    print("================")

div["B"][0]["name"]



























