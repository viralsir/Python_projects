import psycopg2

try:
    # 1. Connect to the database
    connection = psycopg2.connect(
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5433",
        database="ArayanShcoolDB"
    )

    # 2. Create a cursor to perform operations
    cursor = connection.cursor()

    # rollno=int(input("roll no:"))
    # maths=int(input("maths:"))
    # name=input("name:")
    # science=int(input("science:"))
    # total=maths+science
    # #insert query
    # cursor.execute("insert into  student values("+rollno+",34,'ajay',23,1)")

    # select person.name ,person.address , student.course,student.fees from student ,person where person.phonenumber = student.phonenumber and student_phonenumber='08123'
    #
    # cursor.execute("insert into  person values (%s,%s,%s,%s,%s)",
    #                (name, address, phonenumber))
    # connection.commit()
    #
    # cursor.execute("insert into  student  values (%s,%s,%s,%s,%s)",(sid,course,fees,phonenumber))
    # connection.commit()

    # cursor.execute("update student set name='jignesh' where rollno=%s",('4',))
    # connection.commit()

    # cursor.execute("delete from student where rollno='7'")
    # connection.commit()

    #3. select  query
    cursor.execute("SELECT * from student")

    for row in cursor:
         print(row)
         for value in row:
             print(value)
         print("-----------------------")


except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting to PostgreSQL: {error}")

finally:
    # 5. Close communication
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
