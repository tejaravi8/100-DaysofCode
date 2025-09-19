from databse import mydb

teja=mydb.cursor()

teja.execute('use victus')

# teja.execute('''
#              CREATE TABLE marks(
#                 paperid INT PRIMARY KEY AUTO_INCREMENT,
#                 student_id INT,
#                 subject VARCHAR(20),
#                 marks INT,
#                 FOREIGN KEY (student_id) references students(id)
#                 )'''
#             )
# print('table created ')

# teja.execute('show tables')

# # for i in teja:
# #     print(i)
    
# # sql='INSERT INTO marks(student_id,subject,marks) values(%s,%s,%s)'
# # values=[(1,'Maths',85),(2,'Maths',88),(3,'Social',90),(4,'Science',92),(5,'Physics',80),(6,'Drawing',79),(7,'Social',78),(8,'English',90)]
# # teja.executemany(sql,values)

# # mydb.commit()

# # sql='select name,max(marks) from students s,marks m where s.id=m.student_id '
# # teja.execute(sql)

# # res=teja.fetchall()

# # for i in res:
# #     print(i)


# sql='''update marks set paperid=case
# when paperid=1003 then 103
# when 104 then 1004
# when 105 then 1005
# end
# where paperid in(102,103,104)'''

# # teja.execute('select * from marks')
# # rs=teja.fetchall()
# # for i in rs:
# #     print(i)
# # # mydb.commit()


# # teja.execute('select * from students')
# # result=teja.fetchall()

# # for i in result:
# #     print(i)

# sql="""update students set age=case
# when id=1 then 20
# when id=2 then 20
# when id=3 then 20
# else age
# end
# where id in (1,2,3)"""


# teja.execute(sql)
# mydb.commit()

# # teja.execute('select * from students')
# # res=teja.fetchall()
# # print(res)
# # teja.execute(sql)
# # mydb.commit()
# # result=teja.fetchall()
# # for i in result:
# #     print(i)

# sql=input('enter query:')

# teja.execute(sql)
# result=teja.fetchall()
# for i in result:
#     print(i)