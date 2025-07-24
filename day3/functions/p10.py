# Write a function to sum all digits of a number.

def sum():
    num=143
    sum=0
    for i in str(num):
        sum+=int(i)
    return sum

print(sum())