
"""expr = input("Enter a mathematical expression: ")

result = eval(expr)
print(result)"""


def check_express(le):
        if le == "True" or le == "False":
            return 1
        else:
            return 0


le = input("Enter a logical expression")
result = check_express(le)
if result == 1:
    print("It is logical expression")
else:
    print("It is not logical expression")



