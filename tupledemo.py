tupel1=(23,33,44,65,4,5,6)
print(tupel1[0])
print(tupel1[1])
print(tupel1[-1])

#tuple is immutable
print(tupel1[2:5])

#aggregration function
print("no of elements :",len(tupel1))
print("maximum value :",max(tupel1))
print("minimum value :",min(tupel1))
print("Sum :",sum(tupel1))



print("for each")
for item in tupel1:
    print(item)

#tupel1[1]=3434

print("index :",tupel1.index(23))
print("Count :",tupel1.count(32))