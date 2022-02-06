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
          database="LMS_DB")
print(sq)

mycur=sq.cursor()
ans='y'
while ans=='y' or ans=='Y':
    selector=int(input("LMS Data CRUD:  \n 1. Insert Data \n 2. Display Data \n 3. Update Data \n 4. Delete Data \n 5. joins  \n 6. Exit \n "))
    if selector==1:
        more='y'
        while more=='y' or more=='Y':
            enter_id=int(input("Enter user Id:  "))
            enter_email=input("enter  user email: ")
            enterfirst_name=input("Enter user First name:  ")
            enterlast_name=input("Enter user last name:  ")
            enter_password=input("enter your password: ")
            enter_contactno=input("enter your contact no: ")
            enter_varified=input("select 1-varified 0-non varified: ")
            mycur.execute("insert into user_details values({},'{}','{}','{}','{}',{},{})".format(enter_id,enter_email,enterfirst_name,enterlast_name,enter_password,enter_contactno,enter_varified))
            sq.commit()
            more=input("Do you to insert more data ?(y/n)")
    if selector==2:
        mycur.execute("select * from user_details")
        data=mycur.fetchall()
        for i in data:
            print(i)
    if selector==3:
        update_selector=input("what do you want to update ? \n A. employee id \n B. employee name \n")
        if update_selector=='A':
            enter_id_old=int(input("Enter old User Id:  "))
            enter_id_new=int(input("Enter New User Id:  "))
            mycur.execute("update user_details set id={} where id={}".format(enter_id_new,enter_id_old))
            sq.commit()
            print("Data Updated Successfully")
        if update_selector=='B':
            enter_name_old=input("Enter Existing Employee first name:  ")
            enter_name_new=input("Enter new Employee first name:  ")
            mycur.execute("update user_details set first_name={} where first_name={}".format(enter_name_new,enter_name_old))
            sq.commit()
            print("Data Updated Successfully")
    if selector==4:
        delete_selector=input("Choose any one:\n A. Delete all \n B. Selcted Delete data\n")
        if delete_selector=='A':
            mycur.excute("delete from user_details table")
            sq.commit()
            print("Deleted data All")
        if delete_selector=='B':
            enter_id=int(input("Enter user id record to delete:  "))
            mycur.execute("Delete from user_details where id={}".format(enter_id))
            sq.commit()
            print("Data Deleted Successfullly")
    if selector==5:
        join_selector=input("Choose any one:\n a. inner join \n b. left join \n c. right join \n d. cross join \n")
        if join_selector=='a':
            sql_join = "select user_details.first_name,user_details.contact_number,candidate_docs.doc_type from user_details INNER JOIN candidate_docs on user_details.id=candidate_docs.id;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
        if join_selector=='b':
            sql_join = "select user_details.first_name,user_details.contact_number,candidate_docs.doc_type from user_details LEFT JOIN candidate_docs on user_details.id=candidate_docs.id;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
        if join_selector=='c':
            sql_join = "select user_details.first_name,user_details.contact_number,candidate_docs.doc_type from user_details RIGHT JOIN candidate_docs on user_details.id=candidate_docs.id;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
        if join_selector=='d':
            sql_join = "select user_details.first_name,user_details.contact_number,candidate_docs.doc_type from user_details CROSS JOIN candidate_docs;"
            mycur.execute(sql_join)
            data=mycur.fetchall()
            for i in data:
              print(i)
    
    ans=input("Run again (y/n)?")