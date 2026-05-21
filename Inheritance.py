'''
Inheritance : is the proccess by which object of one class can
access or get the properties of object of another class.

category of inheritance
1) Single Inheritance : one class can access or get the properties of only one class at a time.
        A    parent class / base class / super class
        |
        B    child class / derived class / subclass
2) Multilevel Inheritance : continous chain of single inheritance
            A
            |
            B
            |
            C
3) Hyrarchical Inheritance :-  more than one object can access or get the properties of only one class at a time.
                A
          |           |
          B           C

4) Multiple Inheritance : one object can access or get the properties of more than one object at a time.

             A               B
                   |
                   C

5) Hybrid Inheritance : combination of more than one inheritance
            Personal_info
                 |
    Employee                Customer
                   |
                   Dmart


'''
class Personal_info:
    name=""
    address=""
    phone=""

    def setPersonalInfo(self):
        self.name=input("Enter your name: ")
        self.address=input("Enter your address: ")
        self.phone=input("Enter your phone: ")

    def getPersonalInfo(self):
        print("Name : ",self.name)
        print("Address : ",self.address)
        print("Phone : ",self.phone)

class Employee(Personal_info):
    salary=0

    def setEmployeeSalary(self):
        self.salary=input("Enter your salary: ")

    def getEmployeeSalary(self):
        print("Salary : ",self.salary)

class Customer(Personal_info):
    billamount=0
    def setCustomerBill(self):
        self.bill=input("Enter your bill: ")
    def getCustomerBill(self):
        print("Customer Bill: ",self.bill)


class DMart(Employee,Customer):
    location=""

    def setDamartLocation(self):
        self.location=input("Enter your location: ")

    def getDamartLocation(self):
        print("Damart Location: ",self.location)



#single inheritance
# Emp=Employee()
# Emp.setPersonalInfo()
# Emp.setEmployeeSalary()
#
#
# print("=====")
# Emp.getPersonalInfo()
# Emp.getEmployeeSalary()

#multilevel inheritance
# Dmart=DMart()
# Dmart.setPersonalInfo()
# Dmart.setEmployeeSalary()
# Dmart.setDamartLocation()
#
# print("=============")
# Dmart.getPersonalInfo()
# Dmart.getEmployeeSalary()
# Dmart.getDamartLocation()


#hyrarchial inheritance
# Emp=Employee()
# Emp.setPersonalInfo()
# Emp.setEmployeeSalary()
#
# print("=== Emplopyee===")
# Emp.getPersonalInfo()
# Emp.getEmployeeSalary()
#
# Cus=Customer()
# Cus.setPersonalInfo()
# Cus.setCustomerBill()
#
# print("=======Customer====")
# Cus.getPersonalInfo()
# Cus.getCustomerBill()



