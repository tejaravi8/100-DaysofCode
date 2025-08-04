# 6. Sort by Second Element
def sort_by_second(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][1] > lst[j][1]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(sort_by_second([[1, 4], [3, 1], [5, 2]]))