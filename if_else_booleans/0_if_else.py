"""
Draw on whiteboard.
"""

#  Explain that as soon as soon one condition is true, no other is tried.
x = 5
y = 10
if  x > y:
    print("X is largest.")
elif x < y:
    print("Y is largest.")
else:
    print("X & Y are equal.")


# Explain that one is true
if  x > y or x < y:
    print("One is larger than the other.")
else:
    print("X & Y are equal.")

# Explain that both must be true
if  x > y and x > 0:
    print("Something..")



# Explain can do one-liner instead of explicit return True and False
# Bad
def is_valid_name(name):
    if len(name) > 0 and name[0].isupper():
        return True
    else:
        return False

# Good
def is_valid_name(name):
    return len(name) > 0 and name[0].isupper()

# Explain not necessary check == True/False
# Bad
if is_valid_name("Erik") == True:
    print("That's a valid name")
if is_valid_name("Erik") == False:
    print("That's not a valid name")


# Good
if is_valid_name("Erik"):
    print("That's a valid name")
if not is_valid_name("Erik"):
    print("That's a valid name")
