# from pdbc import mydb # type: ignore

# teja=mydb.cursor()


# # teja=mydb.cursor()

# # teja.execute('select * from emp')

# # result=teja.fetchall()

# # for i in result:
# #     print(i)


from pdbc import mydb

a=mydb.cursor()
# a.execute('CREATE DATABASE learning')

# print("Database created successfully")
a.execute("USE learning")
a.execute("""
    CREATE TABLE employees(
    empid int AUTO_INCREMENT PRIMARY KEY,
    empname VARCHAR(30),
    salary int
    )
    """)

print("table created successfully")

sql='insert into employees(empname,salary) values(%s,%s)'

values=(('kesava',1000),('hemanth',1700),('hara',1100))

a.executemany(sql,values)


# print('inserted successfully',a.rowcount)

a.execute('SELECT DATABASE();')
result=a.fetchall()
for row in result:
    print(row)
    
    
    
    

# teja.execute('select * from students')
# teja.fetchall()
# for i in teja:
#     print(i)