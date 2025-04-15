# Ask Duck Debugger AI: What is a good way to name a variable?


# Bad
def check(x):
    if x >= 18:
        return True
    else:
        return False

x = int(input("Type in your age: "))
if check(x):
    print("You are an adult.")
else:
    print("You are a minor.")




# Good
# * Good variable name: *descriptive noun* (object). Singular vs plural, lowercase. 
# * Good constant name: upper case.
# * Good function name: *descriptive verb* (action).
#
# If you have multiple words, join them together with underscores like `input_text` or `speed_of_light`
def age_is_adult(age):
    return age >= 18

age = int(input("Type in your age: "))
if age_is_adult(age):
    print("You are an adult.")
else:
    print("You are a minor.")

