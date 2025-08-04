# 4. Count Even Numbers
def count_evens(nested):
    count = 0
    for sub in nested:
        for num in sub:
            if num % 2 == 0:
                count += 1
    return count

print(count_evens([[1, 2, 3], [4, 6, 7], [8]]))