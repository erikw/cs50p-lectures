import sys

# Bad
number = int(input("Enter a number: ")) # This could raise a.................................................................ValueError
try:
    result = 10 / number
except ZeroDivisionError:
    sys.exit("Cannot divide by zero!")
print(result)


# Good
# number = input("Enter a number: ")
# try:
#     number = int(number)
#     result = 10 / number
# except ZeroDivisionError:
#     sys.exit("Cannot divide by zero!")
# except ValueError:
#     sys.exit(f"The input {number} is not a valid integer.")
# print(result)
