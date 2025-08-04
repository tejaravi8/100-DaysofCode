# 8. Subject-wise Averages
def subject_averages(data):
    math = 0
    eng = 0
    sci = 0
    for student in data:
        math += student[0]
        eng += student[1]
        sci += student[2]
    count = len(data)
    return [round(math/count, 2), round(eng/count, 2), round(sci/count, 2)]

print(subject_averages([[80, 70, 60], [90, 85, 75], [60, 75, 80]]))