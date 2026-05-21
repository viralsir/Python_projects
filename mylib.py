PASSING_MARK=35

def checkmark(mark,subject):
    while mark<0 or mark>100:
        print("invalid marks")
        mark=int(input("enter "+ subject +" mark:"))

    return mark

def isPass_fail(maths,science,english):
    if maths>=PASSING_MARK and science>=PASSING_MARK and english>=PASSING_MARK:
        print("You are Pass")
    else :
        print("You are Fail")


def containDigit(name):
    digit=False
    for char in name:
        if char.isdigit():
            digit=True
            break
    return digit