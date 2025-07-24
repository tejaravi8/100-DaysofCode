# Write a function to count vowels in a string.

def count():
    count=0
    name="racecaAAr".lower()
    for i in name:
        if i in "aeiou":
            count+=1
    return count

print(count())