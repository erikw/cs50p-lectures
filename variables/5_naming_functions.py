# Ask Duck Debugger AI: What is a good way to name a variable?

# Bad
def test_it(a)
    if a == "Hello":
        return "Hi"
    elif a == "Goodbye":
        return "OK see you next time"
    else:
        return "Nice to meet you"

text = input("Type in your greeting: ")
# text = check(text)
text2 = test_it(text)
print(text2)






# Good
# def answer_greeting(greeting)
#     if greeting == "Hello":
#         return "Hi"
#     elif greeting == "Goodbye":
#         return "OK see you next time"
#     else:
#         return "Nice to meet you"

# greeting = input("Type in your greeting: ")
# response = answer_greeting(greeting)
# print(response)
