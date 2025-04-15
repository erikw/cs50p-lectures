"""
* Hierarcy official: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
* Hierarcy image: https://w3.cs.jmu.edu/lam2mo/cs240_2014_08/images/exception_hierarchy.png
"""

# Question: can you see what exceptions can happen?
nbr = int(input("Enter a number: "))
res = 10 / nbr
print(res)




# Handling individually:
# try:
#     nbr = int(input("Enter a number: "))
#     res = 10 / nbr
#     print(res)
# except ValueError:
#     print("Input was not an integer.")
# except ZeroDivisionError:
#     print("Can't divide with zero.")






# Handling together.
# Which is the closest common class anchestor in exception hierarcy?
# try:
#     nbr = int(input("Enter a number: "))
#     res = 10 / nbr
#     print(res)
# except Exception:
#     print("There was an issue with number input and calculation.")



# In most cases, handling individually is better!
