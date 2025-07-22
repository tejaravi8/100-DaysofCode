# 6.	From the string "TupleComprehension", create a tuple containing only the vowels.
res=tuple(i for i in "TupleComprehension" if i in "aeiou")
print(res)
