a = int(input("Please enter number to divide: "))
b = int(input("Please enter number to divide by: "))

try:
    print("{} divided by {} is {}".format(a, b, a/b))
except (ZeroDivisionError, TypeError):
    print("Sorry, can't to that")
