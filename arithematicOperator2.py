"""Write a program that calculates the area of various geometric shapes (e.g., circle, rectangle, triangle)
based on user input. Use appropriate arithmetic operators for the calculations."""

print("Choose a geometric shape:")
print("1-Circle")
print("2-Rectangle")
print("3-Triangle:")
choice = int(input())

if choice == 1:
    r = int(input("Enter the radius of the circle:"))
    print("Area of circle is: ", 3.14*r*r)
elif choice == 2:
    l = int(input("Enter the length of rectangle:"))
    b = int(input("Enter the breadth of rectangle:"))
    print("Area of rectangle is: ", l*b)
elif choice == 3:
    b = int(input("Enter the base of triangle:"))
    h = int(input("Enter the height of triangle:"))
    print("Area of triangle is:", (1/2)*b*h)
