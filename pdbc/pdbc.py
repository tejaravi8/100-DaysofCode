# import mysql.connector

# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Raviteja_41863',
#     database='Victus'
# )

# print('database connected successfully:',mydb.is_connected())
# print()

# mycursor=mydb.cursor()                      # create cursor 

# # mycursor.execute('use victus')         #'variable.execute('sql quary')'

# # a=mycursor.fetchall()                       #fetch data


# # mycursor.execute("SELECT USER();")
# # print("Logged in as:", mycursor.fetchone())

# # mycursor.execute("SELECT DATABASE();")
# # print("Current Database:", mycursor.fetchone())
# # for table in a:
# #     print(table)
# # print(a)

# # mycurser.close()
# # mydb.close()

# # print()
# print('database connected successfully:',mydb.is_connected())

# mycursor.execute('select * from emp')
# a=mycursor.fetchall()
# for i in a:
#     print(i)


import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raviteja_41863',
)

print('connected successfully',mydb.is_connected())
