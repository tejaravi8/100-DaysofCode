# From the string "TupleComprehension", create a tuple containing only the vowels. 

new=tuple(i for i in "TupleComprehension" if i in "AEIOUaeiou")
print(new)