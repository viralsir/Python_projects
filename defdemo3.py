import mylib
from mylib import checkmark,isPass_fail

rollno=int(input("Enter your roll no."))
name=input("Enter your name.")
while mylib.containDigit(name)==True:
    print("Digit are not allowed")
    name=input("Enter your name.")
maths=checkmark(int(input("Enter Maths marks:")),"Maths")
science=checkmark(int(input("Enter Science marks:")),"science")
english=checkmark(int(input("Enter English marks:")),"English")


print("Roll No:",rollno)
print("Name:",name)
print("Maths:",maths)
print("Science:",science)
print("English:",english)
isPass_fail(maths,science,english)
