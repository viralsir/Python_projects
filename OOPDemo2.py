class student:
    name=""
    age=0
    maths=0
    science=0
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    def entry(self):
        self.name = input("Enter your name: ")
        self.maths = int(input("Enter your maths: "))
        self.science = int(input("Enter your science: "))

    def pass_fail(self):
        if self.maths >= 35 and self.science >= 35:
            print("You are Pass")
        else:
            print("You are Fail")

    def view(self):
        print("Name :", self.name)
        print("Maths :", self.maths)
        print("Science :", self.science)
        self.pass_fail()



studentlist=[]
for i in range(2):
    studentobj=student()
    studentobj.entry()
    studentlist.append(studentobj)

print("======================")
for studentobj in studentlist:
    studentobj.view()

    print("-----------------------")

