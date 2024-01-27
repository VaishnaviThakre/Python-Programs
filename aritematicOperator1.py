"""Create a program that takes two numbers as input and allows the user to perform basic arithmetic operations
(addition, subtraction, multiplication, division) using arithmetic operators."""

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print("Enter operation to perform:")
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
choice = int(input())

if choice == 1:
    print("Addition of ", a, "", b, "is: ", a+b)

elif choice == 2:
    print("Subtraction of ", a, "", b, "is: ", a-b)
elif choice == 3:
    print("Multiplication of ", a, "", b, "is: ", a*b)
elif choice == 4:
    print("Division of ", a, "", b, "is: ", a/b)
