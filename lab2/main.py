import re
import MySQLdb
from employee import Employee
from person import Person
from office import Office

ptrn = r'^[a-zA-z0-9]+@[a-z]+.[a-z]{2,4}$'

office = Office("OSD")
print ('1) Show All Employees\n2) Select Employee\n3) Add Employee\n4) Delete Employee\n5) Exit')
choice = int(input("enter your choice: "))
while choice!= 5:
    if choice == 1:
        office.get_all_employees()
    elif choice == 2:
        empid= int (input("enter employee id to search : "))
        office.get_employee(empid)
    elif choice == 3:
        x = input("do you want to add new employee : [y/n] ")
        while x != "n":
            user = input("if manager press 1 \nif normal employee press 2 : ")
            print("Enter your data: ")
            id =int (input("ID: "))
            email = input("Email: ")
            work_hours =int (input("Work Hours: "))
            salary =int(input("Salary: "))
            emp = Employee(id,email,work_hours , salary , user)
            office.hire(emp)
            x = input("do you want to add new employee: [y/n] ")
    elif choice==4:
        empid= int (input("enter employee id to delete : "))
        office.fire(empid)
    print ('1) Show All Employees\n2) Select Employee\n3) Add Employee\n4) Delete Employee\n5) Exit')
    choice = int(input("enter your choice: "))





