# import mysql.connector

# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Raviteja_41863'
# )

# print('connection status:',mydb.is_connected())
# # teja=mydb.cursor()


# # teja.execute('CREATE DATABASE IF NOT EXISTS learning')

# # teja.execute('show databases')
# # for i in teja:
# #     print(i)


import mysql.connector

mydatabase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raviteja_41863',
    database='hari'
)

pablo=mydatabase.cursor()

pablo.execute('use hari')

print(mydatabase.is_connected())

# pablo.execute('create table durva(uid int PRIMARY KEY AUTO_INCREMENT,movie varchar(30) Not null ,results varchar(10))')

# pablo.execute('desc durva')
# result=pablo.fetchall()
# for i in result:
#     print(i)


pablo.execute('select * from durva')
res=pablo.fetchall()

print(res)



mydatabase.close()

print(mydatabase.is_connected())