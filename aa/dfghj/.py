# # # # # try:
# # # # #     a=-10
# # # # #     if a<0:
# # # # #         print(a)
# # # # #         # raise ReferenceError("raviteja is noob")
# # # # # except TypeError:
# # # # #     print(TypeError)

# # # def withdraw(balance, amount):
# # #     if amount > balance :
# # #         raise ValueError("Insufficient balance!")
# # #     elif amount<0:
# # #         raise ValueError("Can't be in negitive")
# # #     return balance - amount

# # # try:
# # #     balance = 5000
# # #     amount = int(input("Enter amount to withdraw: "))
# # #     new_balance = withdraw(balance, amount)
# # #     print(f"✅ Withdrawal successful. Remaining balance: ₹{new_balance}")
# # # except ValueError as v:
# # #     print("gdg")
# # # except TypeError:
# # #     print("ghhd")


# # # # a=int(input("en:"))
# # # # b=int(input("t:"))
# # # # if type(a)==int and type(b)==int:
# # # #     print(a*b)
# # # # else:
# # # #     print("ee")

# # cart = {"Apples": 3, "Bananas": 0, "Mangoes": 5}

# # for item, qty in cart.items():
# #     try:
# #         if qty <= 0:
# #             raise ValueError(f"{item} is out of stock.")
# #         print(f"{item} available: {qty} left.")
# #     except ValueError as e:
# #         print("Error:", e)

# def validate_marks(marks):
#     for mark in marks:
#         try:
#             if not isinstance(mark, int):
#                 raise TypeError(f"Invalid type: {mark} is not an integer.")
#             if mark < 0 or mark > 100:
#                 raise ValueError(f"Invalid mark: {mark}. Must be 0–100.")
#             print(f"Valid mark: {mark}")
#         except (TypeError, ValueError) as e:
#             print("Error:", e)

# student_marks = [95, 102, "A+", 75, -5]
# validate_marks(student_marks)

# a=int(input(""))

# # print(a)

# result = "10" + 5  
# print(result)

# a=[1,2,3,4,5]
# print(a[:])

a={"teja":5,
   "t":3}
print(a["teja"])
# print(a.get("te"))