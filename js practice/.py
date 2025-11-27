# class MyNumber:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return MyNumber(self.value + other.value)

#     def __str__(self):
#         return f"MyNumber with value: {self.value}"

# # Using dunder methods implicitly
# num1 = MyNumber(5)
# num2 = MyNumber(10)

# num3 = num1 + num2  # Calls __add__
# print(num3)        # Calls __str__