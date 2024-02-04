# Define a function to evaluate the expression
def evaluate_expression(a, b, c, d, e):
    result = a * b + c / d - e
    return result

# Get user input for variables a, b, c, d, and e
a = float(input("Enter the value for 'a': "))
b = float(input("Enter the value for 'b': "))
c = float(input("Enter the value for 'c': "))
d = float(input("Enter the value for 'd': "))
e = float(input("Enter the value for 'e': "))

# Evaluate the expression in different orders
result1 = a * b
result2 = c / d
result3 = result1 + result2
result4 = result3 - e

# Display the results
print("Results of different order of evaluation:")
print(f"a * b + c / d - e = {evaluate_expression(a, b, c, d, e)} (Original Order)")
print(f"(a * b) + (c / d) - e = {result4} (Order: (a * b) + (c / d) - e)")
print(f"a * (b + c) / d - e = {result3} (Order: a * (b + c) / d - e)")
print(f"a * b + (c / (d - e)) = {a * b + (c / (d - e))} (Order: a * b + (c / (d - e)))")
