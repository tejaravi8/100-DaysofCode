# Write a function to check if a string is a palindrome.

def palindrome():
    name="racecar"
    rev=""
    for i in name:
        rev=i+rev
    if name==rev:
        return "palindrome"
    else:
        return "Not a Palindrome"      
print(palindrome())