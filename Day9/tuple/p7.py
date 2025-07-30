#  Create a tuple of squares of numbers from 1 to 15 using comprehension. 

a=tuple(i**2 for i in range(1,16))
print(a)