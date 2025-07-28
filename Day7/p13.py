#  Count how many times digit 7 appears between 1 to 100.

count = 0
for i in range(1, 101):
    count += str(i).count('7')
print(count)
