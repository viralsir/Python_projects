name="hello welcome to the world of python"
# print(name)
# print(name[0])
# print(name[-1])
# print(name[2:5])
# #name[2]='t'
#
# print(name.upper())
# print(name[0].upper())
# print(name[0])
# print(name.replace('hello','hi'))
# print(name.replace(' ','-'))
# print(name.capitalize())

for character in name:
     if character.isalpha():
        print(character," - alphabet")
     elif character.isdigit():
         print(character," - digit")
     elif character.isspace():
         print(character," - space")
     else:
         print(character," - symbol")


name1="Vimal"
name2="shah"
name3=name1+name2
print(name3)
name4=name1*2
print(name4)

print(name.split())
print(name.split("o"))
print(name.index("o",5))


