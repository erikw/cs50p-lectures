"""
On a whiteboard, write
* the following code
* one section with variables and arrows to
* one section showing the memory objects

Write labels on a pice of paper and put on physical objects.
"""




a = "text1"
b = "text2"
print(a)
print(b)

b = a
print(a)
print(b)


a = "text3"
# Note that variable b still points to "text1".
# Note that "text1" no longer has any references and is garbage collected.
print(a)
print(b)


c = a.replace("3", "4")
# Note that "text3" is not changed, a copy is created and returned.
print(c)
