file1=open("first.txt","a")

id=int(input("enter id"))
name=input("enter name")

print(id,name,file=file1)

file1.close()

file2=open("first.txt","r")

print(file2.read())
for line in file2.read():
    print(line)

file2.close()
print("=======")

with open("first.txt","r") as file:
    print(file.read())