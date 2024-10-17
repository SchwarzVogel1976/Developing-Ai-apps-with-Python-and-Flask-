def area_of_rectangle(x, y):
    return x*y

print("Enter Length and Breadth of Rectangle: ", end="")
l = float(input())
b = float(input())
a = area_of_rectangle(l, b)
print("\nArea = ", a)


def area_of_circle(rad):
    return 2 * 3.14 * rad

print("Enter Radius of Circle: ", end="")
r = float(input())
c = area_of_circle(r)
print("\nCircumference = {:.2f}".format(c))
