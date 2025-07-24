# Write a function to return the factorial of a number.

def fact(a):
    return [i for i in range(1,a+1) if a%i==0]

i=int(input("enter a num:"))
print(fact(i))