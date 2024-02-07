def fun(a):
    if a < 5:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

        # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(4)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")