title=["Roll No:","Name:","Maths:","Science:","English:"]
studentlist=[]
option=1
while option!=3:
    print("\t\t\t Student Info")
    print("\t\t\t 1. Add Student")
    print("\t\t\t 2. View Student")
    print("\t\t\t 3. Exit")
    option=int(input("Enter your choice:"))
    if option==1:
        option2="y"
        while option2.lower()=="y":
            student={}
            for t in title:
                if t=="Roll No:" or t=="Name:":
                    student[t]=input("Enter student "+t)
                else:
                    student[t]=int(input("Enter student "+t))
            studentlist.append(student)
            option2=input("Do you want to add another student?(y/n)")

    elif option==2:
        print("\t\t\t Student Info")
        for student in studentlist:
            for key,value in student.items():
                print(key,value)
            print("=========================")
    elif option==3:
        print("\t\t you are exited")
    else :
        print("\t\t Wrong Choice selected try again")
