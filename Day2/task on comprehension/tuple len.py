# 10.	 From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters

res=tuple(i for i in ["cat","dog","parrot","cow"] if len(i)>3)
print(res)