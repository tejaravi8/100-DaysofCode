# 1. Flatten a deeply nested list (Simple Version)
def flatten(nested):
    result = []
    for item in nested:
        if type(item) == list:
            for sub_item in item:
                if type(sub_item) == list:
                    result.extend(sub_item)
                else:
                    result.append(sub_item)
        else:
            result.append(item)
    return result

print(flatten([[1, 2, [3, 4]], 5, [6, [7, 8]]]))