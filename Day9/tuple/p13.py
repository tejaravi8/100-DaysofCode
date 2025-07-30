# 6)  From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters.

anim=["cat", "dog", "parrot", "cow"]
new=tuple(i for i in anim if len(i)>3)
print(new)