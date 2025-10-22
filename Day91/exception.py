# # # # try:
# # # #     a=10
# # # #     b=0
# # # #     print(a/b)
# # # #     print("zero can't be devided")
# # # # except ZeroDivisionError:
# # # #     print("Something went wrong")

# # # # try:
# # # #     a = int(input("Enter a number: "))
# # # #     print(10/a)
# # # # except ZeroDivisionError: # zero can't divided with any integer
# # # #     print("You cannot divide by zero!")
# # # # except ValueError:  # based on value
# # # #     print("Please enter a valid number!")
# # # # else:
# # # #     print(10/a)
# # # # finally:
# # # #     print("done")

# # # try:
# # #     num = input("Enter a number: ")
# # #     print(10 / num)
# # # except ZeroDivisionError:
# # #     print("Cannot divide by zero!")
# # # except TypeError:
# # #     print("sorry bro")
# # # else:
# # #     print("Division successful.")
# # # finally:
# # #     print("End of program.")

# # age = int(input("Enter your age: "))
# # if age < 18:
# #     raise ValueError("You must be 18 or older!")
# # else:
# #     print("Access granted.")

# age = int(input("Enter your age: "))

# if age < 0:
#     raise ValueError("Age cannot be negative!")
# elif age < 18:
#     raise ValueError("You must be 18 or older!")
# else:
#     print("Access granted.")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("❌ Error caught:", e)
else:
    print(divide(10, 5))
    
    