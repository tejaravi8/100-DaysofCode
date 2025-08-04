# 2. Maximum Sublist Sum
def max_sum_sublist(lst):
    max_list = lst[0]
    for sublist in lst:
        if sum(sublist) > sum(max_list):
            max_list = sublist
    return max_list

print(max_sum_sublist([[2, 3], [10, -2, 1], [4, 5, 6]]))