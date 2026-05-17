'''
   loop  :
        1) while
             syntax :
                        while condition :
                                true part;
                                    statment
                                 incrment / decrment of variable
        2) for
                   a) for iterator
                   b) for each   -> data structure

'''
# start=1
# while start<=100:
#     print(start)
#     start+=10

# start=int(input("Enter start number: "))
# end=int(input("Enter end number: "))
# sum=0
# while start<=end:
#     print(start)
#     sum=sum+start
#     start+=10
#
# print("Sum :",sum)


# start=1
# no=int(input("enter no:"))
# while start<=10:
#     print(no," * ",start," = ",no*start)
#     start=start+1


# no=int(input("enter no:"))
# start=1
# print("Divisior :")
# while start<=no:
#     if no%start==0:
#         print(start)
#     start=start+1

#nested while
# start=1
# while start<=5:
#     nstart=1
#     while nstart<=start:
#         print(nstart,end="")
#         nstart=nstart+1
#     print("")
#     start=start+1



start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
while start<=end:
    no=start;
    j=1
    while j<=10:
       print(no," * ",j," = ",no*j)
       j=j+1
    print("")
    start=start+1


