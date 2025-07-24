# Write a function to reverse a string.

def rev(name):
    name=name
    re=""
    for i in range(len(name)-1,-1,-1):
        re+=name[i]
    print(re)
rev("teja")