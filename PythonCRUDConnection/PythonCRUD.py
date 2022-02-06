'''
@Author: Hitesh Patil
@Date: 20-01-2022 13:05:46
@Last Modified by: Hitesh Patil
@Last Modified time: 22-01-2022 09:50:56
@Title : All CRUD Operation 
'''
from ctypes.wintypes import DOUBLE
from tokenize import Double
import mysql.connector

sq= mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="Hitesh@1234",
          database="test_CRUD")
print(sq)

mycur=sq.cursor()
ans='y'
while ans=='y' or ans=='Y':
    selector=int(input("CRUD operation:  \n 1. Insert Data \n 2. Display Data \n 3. Update Data \n 4. Delete Data \n 5. joins  \n 6. Add foreign key \n 7. Add Procedure \n 8. Exit \n "))
    if selector==1:
        more='y'
        while more=='y' or more=='Y':
            enter_id=int(input("Enter Employee Id:  "))
            enter_name=input("Enter Employee name:  ")
            enter_salary=input("enter salary: ")
            enter_dept=input("enter department: ")
            mycur.execute("insert into emp values({},'{}',{},'{}')".format(enter_id,enter_name,enter_salary,enter_dept))
            sq.commit()
            more=input("Do you to insert more data ?(y/n)")
    if selector==2:
        mycur.execute("select * from emp")
        data=mycur.fetchall()
        for i in data:
            print(i)
    if selector==3:
        update_selector=input("what do you want to update ? \n A. employee id \n B. employee name \n")
        if update_selector=='A':
            enter_id_old=int(input("Enter old Employee Id:  "))
            enter_id_new=int(input("Enter New Employee Id:  "))
            mycur.execute("update emp set E_id={} where E_id={}".format(enter_id_new,enter_id_old))
            sq.commit()
            print("Data Updated Successfully")
        if update_selector=='B':
            enter_name_old=input("Enter Existing Employee name:  ")
            enter_name_new=input("Enter new Employee name:  ")
            mycur.execute("update emp set E_Name={} where E_Name={}".format(enter_name_new,enter_name_old))
            sq.commit()
            print("Data Updated Successfully")
    if selector==4:
        delete_selector=input("Choose any one:\n A. Delete all \n B. Selcted Delete data\n")
        if delete_selector=='A':
            mycur.excute("delete from emp table")
            sq.commit()
            print("Deleted data All")
        if delete_selector=='B':
            enter_id=int(input("Enter id record to delete:  "))
            mycur.execute("Delete from emp where E_id={}".format(enter_id))
            sq.commit()
            print("Data Deleted Successfullly")
    if selector==5:
        join_selector=input("Choose any one:\n a. inner join \n b. left join \n c. right join \n d. cross join \n")
        if join_selector=='a':
            sql_join = "SELECT compare.customer_Name, compare.income, emp.dept_name FROM compare   INNER JOIN emp  ON compare.id = emp.E_id;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
        if join_selector=='b':
            sql_join = "SELECT compare.customer_Name, compare.income, emp.dept_name FROM compare   LEFT JOIN emp  ON compare.id = emp.E_id;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
        if join_selector=='c':
            sql_join = "SELECT compare.customer_Name, compare.income, emp.dept_name FROM compare   RIGHT JOIN emp  ON compare.id = emp.E_id;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
        if join_selector=='d':
            sql_join = "SELECT compare.customer_Name, compare.income, emp.dept_name  FROM compare   CROSS JOIN emp;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
    if selector==6:
        FKey_selector=input("Choose any one:\n a. Add Foreign key \n b. Drop Foreign Key \n")
        if FKey_selector=='a':
            sql_addkey = "ALTER TABLE compare ADD CONSTRAINT fk_emp FOREIGN KEY (id) REFERENCES emp(E_id) ON DELETE CASCADE ON UPDATE RESTRICT;"
            mycur.execute(sql_addkey)
            
        if FKey_selector=='b':
            sql_dropkey = "ALTER TABLE compare DROP FOREIGN KEY fk_emp;"
            mycur.execute(sql_dropkey)
    if selector==7:
        procedure_selector=input("Choose any one:\n a. create proce. all data \n b. create prced. find the data \n")
        if procedure_selector=='a':
            sql_getall = "delimiter && create employee_data() begin select * from employee;  end&&"
            mycur.execute(sql_getall)
            
        if procedure_selector=='b':
            sql_dropkey = "ALTER TABLE compare DROP FOREIGN KEY fk_emp;"
    ans=input("Run again (y/n)?")

#try exception