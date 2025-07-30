# From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters.
 
animals=["cat","dog","parrot","cow"]
a=tuple(i for i in animals if len(i)>3)
print(a)