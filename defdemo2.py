# def sub(no1,no2):
#     return no1-no2
#
#
# print("Substraction :",sub(23,3))
# print("Substraction :",sub(no2=3,no1=23))

#default argument function
def total(no1=0,no2=0,no3=0):
    return no1+no2+no3


print("total :",total(23,23,33))
print("total :",total(23,23))
print("total :",total(23))
print("total :",total())
