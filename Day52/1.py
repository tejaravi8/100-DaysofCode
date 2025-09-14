# side=5
# square=side*side
# print("Area of Square:",square)

# l=6
# b=4
# print('area of rectangle:',l*b)

# b=8
# h=5
# print('area of triangle:', (1/2)*b*h )

# side=5
# print(4*side)
# l,b=5,6
# print('perimeter of rectangle:',2*(l+b))

# side=5
# side2=3
# side3=4
# print('perimeter of triangle:',side+side2+side3)

amount=3700
thousands=amount//1000
remain=amount-thousands*1000
hundreads=remain//500
remain=remain-hundreads*500

print('1000s:',thousands,'500s:',hundreads)