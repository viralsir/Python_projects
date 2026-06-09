iserror=True

while iserror:

    try:
        no1=int(input("enter no1"))
        no2=int(input("enter no2"))

        ans=no1/no2

        print(ans)
        iserror = False
    except ZeroDivisionError:
        print("zero invalid input")
    except ValueError:
        print("Character are not allowed")
    finally:
        print(" program terminated")

