# set1={23,23,"vimal",34,55}
# print(set1)
# set1.add(555)
# print(set1)
# print(set1.remove(55))
# print(set1)
#
# for value in set1:
#     print(value)

# set1={23,23,33,44,55,66}
# print("no of elements :",len(set1))
# print("maximum element:",max(set1))
# print("minimum element:",min(set1))
# print("Sum of element :",sum(set1))

set1={1,2,3,4,5}
set2={4,5,6,7,8}

set3=set1.intersection(set2)
set4=set1 & set2
print(set3)
print(set4)

set3=set1.difference(set2)
set4=set2-set1
print(set3)
print(set4)

set3=set1.union(set2)
set4=set1 | set2
print(set3)
print(set4)

set3=set1.symmetric_difference(set2)
set4=set1 ^ set2
print(set3)
print(set4)
