list1=[x for x in range(1,10)]
print(list1)
list1=[x*x for x in range(1,10)]
print(list1)
list1=[x+5 for x in range(1,10)]
print(list1)
list1=[x for x in range(1,10) if x%2==0]
print(list1)
marks_list=[24,5,55,66,3,43]
pass_list=[ m for m in marks_list if m>=35]
print(pass_list)