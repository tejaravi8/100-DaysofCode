# 5. Replace Target Number with -1
def replace_number(lst, target):
    result = []
    for sub in lst:
        new_sub = []
        for num in sub:
            if num == target:
                new_sub.append(-1)
            else:
                new_sub.append(num)
        result.append(new_sub)
    return result

print(replace_number([[1, 2, 3], [4, 2, 5]], 2))