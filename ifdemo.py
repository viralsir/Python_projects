'''

  condition control structure
  if
   syntax :
                if condition :
                    true part;
                    statement
                elif  condition:
                    false part;
                    statement
                else :
                    false part;
                    statement

       Relational Operator
       Operator                     symbol
       grather than                 >
       less than                    <
       equal to                     ==
       not equal to                 !=
       grater than or equal to       >=
       less than or equal to         <=

      logical operator
      opeator               symbol
      and                   and
      or                    or
      not                   not

'''
no1=int(input("Enter no1: "))
no2=int(input("Enter no2: "))
no3=int(input("Enter no3: "))
if no1>0 and no2>0 and no3>0:
    if no1>no2 and no1>no3:
        print(no1," is maximum number")

    elif no2>no1 and no2>no3:
        print(no2," is maximum number")
    else:
        print(no3," is maximum number")

else :
    print("invalid input")
















