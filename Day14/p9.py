# 9. Check Structural Equality
def same_structure(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if type(lst1[i]) == list and type(lst2[i]) == list:
            if len(lst1[i]) != len(lst2[i]):
                return False
        elif type(lst1[i]) != type(lst2[i]):
            return False
    return True

print(same_structure([[1, 2], [3, 4]], [["a", "b"], ["c", "d"]]))