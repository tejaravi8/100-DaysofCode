# # # # # class Student:
# # # # #     namex="hello"

# # # # #     def __init__(self,name,salary):
# # # # #         self.name=name
# # # # #         self.salary=salary
# # # # #         print(namex)
     
# # # # #     def show(self):
# # # # #         print(self.name)
# # # # #         print(self.salary)
     
# # # # # # namee="ravi"
# # # # # obj1=Student("teja",10000)
# # # # # # obj1.show()
# # # # # Student.name="pablo"
# # # # # print(Student.name)


# # # # # @classmethod

# # # # class Company:
# # # #     com_name="TCS"
# # # #     def __init__(self,salary):
# # # #         self.name=Company.com_name
# # # #         self.salary=salary
    
# # # #     @classmethod  
# # # #     def change_company(cls,newname):
# # # #         cls.com_name=newname
    
# # # #     def display(self):
# # # #         print(self.com_name)

# # # # obj1=Company(50000)

# # # # Company.change_company("Wipro")

# # # # print(Company.com_name)

# # # class BankAccount:
# # #     bank_name = "SBI"     # CLASS VARIABLE

# # #     def __init__(self, name, balance):
# # #         self.name = name  # INSTANCE VARIABLE
# # #         self.balance = balance  # INSTANCE VARIABLE

# # # acc1 = BankAccount("Teja", 2000)

# # # print(acc1.balance)

# # class Student:
# #     school="ZPHS"
    
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
        

# # teja=Student("teja",99)
# # ravi=Student("ravi",98)

# # print(teja.name,teja.marks,teja.school)
# # print(ravi.name,ravi.marks,ravi.school)

# class Student:
    
#     school="zphs"
#     def __init__(self,name,marks,roll):
#         self.name=name
#         self.__marks=marks
#         self._roll=roll
    
#     def show_mark(self):
#         return self.__marks
    
#     def edit(self,new_mark):
#         if new_mark>85:
#             return self.__marks+10
#         else:
#             return self.__marks-10

# obj=Student("teja",86,1)
# # mar=obj.edit(86)
# # print(mar)
# print(obj._Student__marks)

class Employee:
    
    def __init__(self,name,sal):
        self.name=name
        self.__sal=sal
        
    @property
    def getsal(self):
        return self.__sal
    
    @getsal.setter
    def getsal(self,salary):
        if salary<=50000:
            self.__sal=self.__sal*1.10
            # return self.__sal
        else:
            self.__sal=self.__sal*1.05
            # return self.__sal

obj=Employee("raviteja",50000)
obj.getsal=55000
print(obj.getsal)
# print(m)
