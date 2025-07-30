# From a list of names, create a tuple of names that start with the letter 'A' or 'a' 


a=['teja','ajay','Apple','pablo','charan','anya']
new=tuple(i for i in a if i.startswith("a") or i.startswith("A"))
print(new)