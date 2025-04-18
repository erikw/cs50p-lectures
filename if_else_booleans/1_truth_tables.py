"""
Draw on whiteboard.

# Truth tables
Two expressions:
X := name.islower()
Y := d > 5
we can combine in an expression in an if:
if X and Y:
if X or Y:
if not X or Y:
etc.


X | Y | X and Y
--------------
F | F | F
T | F | F
F | T | F
T | T | T



X | Y | X or Y
--------------
F | F | F
T | F | T
F | T | T
T | T | T


X |  not X
-----------
F |  T
T |  F



# Short-circuit 
X or Y # If X is True, Y is not even considered. 



# Associativity and precedence
Ref: https://www.programiz.com/python-programming/precedence-associativity
The operators bind from hard to low: not, and, or
Similar to math:
5 + 2 * 3  => 5 + (2 * 3)

X or Y and Z => X or (Y or Z)
not X and Y  => (not X) and Y
X and not Y or Z  => (X and (not Y)) or Z


# Invert an boolean expression
a.k.a. De Morgan's laws

Similar to math:
-1 * (5 + 2) == -5 - 2
-1 * (5 - 2) == -5 + 2


not (X and Y) == not X or not Y
not (X or Y) == not X and not Y
not (not X or Y) == X and not Y
"""
