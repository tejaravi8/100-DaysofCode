import csv

with open('ttt.csv','w',newline='') as t:
    obj=csv.writer(t)
    obj.writerow(['roll','s_name','fee'])
    
    for x in range(2):
        roll=input("enter roll number: ")
        name=input("enter your name: ")
        fee=input("enter your salary: ")
        
        obj.writerow([roll,name,fee])

# t=open("teja.csv",'w',newline="")
# data=csv.writer(t)
# data.writerow(['roll','name','fee'])

# for i in range(2):
#     roll=input("enter your roll")
#     name=input("enter name")
#     fee=input("enter your fee")
    
#     data.writerow([roll,name,fee])


with open("teja.csv",'r') as t:
    dat=csv.reader(t)
    for x in dat:
        print(x)
        
        
# data bse : realational tables  and non relational data base   :   keys and values ( like mango db)
# collection of tables

# data base : my sql    dcl dql dml like commands...

# sql: laguage is used to instruct my sql

# pdpc 