# Python Problem-Solving Set (Post-Core Level)
# 1. Logic & Loops

# Write a program to print all numbers between 1 and 100 that are divisible by 3 but not by 5.

# Given a number, check if it is an Armstrong number (153 → 1³ + 5³ + 3³ = 153).

# Generate the first 20 Fibonacci numbers without using recursion.

# Count how many prime numbers are there between 1 and 500.

# Reverse a number without using string conversion.

# 2. Strings

# Find the most frequent character in a given string.

# Remove all special characters from a string, keeping only letters and numbers.

# Check if two strings are anagrams of each other.

# Replace all spaces in a string with underscores (_).

# Capitalize the first letter of each word without using .title().

# 3. Lists & Dictionaries

# Merge two dictionaries into one (values of same keys should be summed).

# Find the second smallest element in a list without using sorting functions.

# Remove duplicates from a list without using set().

# Count the frequency of each element in a list using a dictionary.

# Given a dictionary of students with marks, print the student(s) with the highest marks.

# 4. File Handling

# Create a text file and store 10 random numbers in it, then read the file and print only even numbers.

# Count the total number of words in a given text file.

# Copy the contents of one file into another.

# Read a CSV file of student names & scores, and print the top 3 scorers.

# Append a line at the end of an existing file without overwriting.

# 5. Bonus – Real-Life Logic

# ATM Simulation:

# Take a user’s balance as input.

# Ask for withdrawal amount.

# Deduct only if funds are sufficient; otherwise show an error.

# Library System:

# Add books to inventory (dict with book name & stock).

# Borrow books (decrease stock).

# Return books (increase stock).

# Weather Data Analysis:

# Given a list of daily temperatures, find:

# Highest temperature

# Lowest temperature

# Average temperature.

# Simple Login System:

# Store usernames & passwords in a dict.

# Ask for login, check credentials, allow 3 attempts max.

# Shopping Cart:

# Add items with prices.

# Show total bill.

# Apply discount if bill > 1000.



# x = ["apple", "banana"]
# y = ("apple", "banana")
# x=y.index('apple')
# print(x)






# # hello="""Lorem ipsum dolor sit amet,
# # consectetur adipiscing elit,
# # sed do eiusmod tempor incididunt
# # ut labore et dolore magna aliqua."""
# # print(hello)

# class institute:
#     name='10k coders'
    
#     def __init__(self,fee):
#         self.fee=fee
#         print(f'fee is {self.fee}')
    
#     def sir(self,name):
#         self.name=name
#         print(f'sir name is {self.name}')
        

#     @classmethod
#     def change(cls):
#         cls.name='teja'
#         print(cls.name)
        
# ball=institute(100)
# ball.sir('teja')
# institute.change()
# print(institute.name)

# class Student:
#     def __init__(self, name, marks):
#         self.__marks = marks   # private variable
#         print(self.__marks)

#     def get_marks(self):
#         return self.__marks    # controlled access

# s = Student("Teja", 90)
# print(s.__marks)   #❌ Error
# print(s.get_marks())  # ✅ Access through method


# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#         # print(self.__balance) # private

#     def deposit(self, amount):
#         print(self.__balance)
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount(500)

# acc.deposit(100)
# print(acc.get_balance())  # ✅ 1500
# # print(acc.__balance)    ❌ Error


# from abc import ABC, abstractmethod

# class Shape(ABC):   # Abstract Class
#     @abstractmethod
#     def area(self):   # Abstract Method
#         pass

#     # @abstractmethod
#     # def perimeter(self):
#     #     pass

#         # 78.5
# # print("Perimeter:", c.perimeter()) # 31.4

# from abc import ABC,abstractmethod

# class find(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def area2(self):
#         pass
    
# class show(find):
    
#     def __init__(self,rad):
#         self.rad=rad
        
#     def area(self):
#         return 3.14 *self.rad*self.rad
    
#     def area2(self):
#         return 3.14*self.rad*self.rad*2


from teja2 import parent

class mom(parent):
    
    def child1(self,age):
        self.age=age
        return self.age+5
    
    def child2(self,age):
        self.age=age
        return age

        
    