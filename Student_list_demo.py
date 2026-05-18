#student_list=[ [1,"vimal",34,33,44] ,[2,"amit",34,33,44] ]
studentlist=[]
Passing_Mark=35
title=["Roll No:","Name:","Maths:","Science:","English:","SS:"]
option=1
while option!=3:
    print("\n\t\t\t Student Info")
    print("\t\t Press 1 for Entry")
    print("\t\t Press 2 for View")
    print("\t\t Press 3 for Exit")

    option=int(input("Enter your choice:"))
    if option==1:
        option2="y"
        while option2=="Y" or option2=="y":
            student=[]
            for t in title:
                if t=="Roll No:" or t=="Name:":
                    student.append(input("Enter "+t))
                else:
                    mark=int(input("Enter "+t))
                    while mark<0 or mark>100:
                        print("Enter a mark between 1 and 100")
                        mark=int(input("Enter "+t))
                    student.append(mark)

            studentlist.append(student)
            option2=input("Do you want to continue? (y/n) :")
    elif option==2:
        print("\n\t\t\t View")
        for student in studentlist:
            isPass=True
            for t,value in zip(title,student):
                print(t,value)
                if t!="Roll No:" and t!="Name:":
                    if value<Passing_Mark:
                        isPass=False
            if isPass==True:
                print("You are Pass")
                total=sum(student[2:])
                avg=total/len(student[2:])
                print("Total:",total)
                print("Average:",avg)
            else :
                print("You are Fail")
            print("================================")
    elif option==3 :
        print("\n\t\t\t Exit")
    else :
        print("\n\t\t\t Invalid Input")

