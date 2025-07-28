# #  Sort a dictionary by values 

dic={"teja":21,
     "ravi":20,
     "XXL":22}

sorted_dict=dict(sorted(dic.items(),key=lambda x:x[1]))
print(sorted_dict)
