class student:
    name=""
    age=0
    maths=0
    science=0
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

studentlist=[]
for i in range(2):
    studentobj=student()
    studentobj.name=input("Enter your name: ")
    studentobj.maths=int(input("Enter your maths: "))
    studentobj.science=int(input("Enter your science: "))

    studentlist.append(studentobj)

print("======================")
for studentobj in studentlist:
    print(studentobj)
    print("Name :",studentobj.name)
    print("Maths :",studentobj.maths)
    print("Science :",studentobj.science)
    print("-----------------------")



# st1=student()
# st2=student()
# st1.name=input("Enter your name")
# st1.maths=int(input("Enter your maths"))
# st1.science=int(input("Enter your science"))
#
#
# st2.name=input("Enter your name")
# st2.maths=int(input("Enter your maths"))
# st2.science=int(input("Enter your science"))
#
# print(st1)
# print(st1.name)
# print(st1.maths)
# print(st1.science)
# print("============")
# print(st1.name)
# print(st2.age)