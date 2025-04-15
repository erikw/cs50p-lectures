# NOTE skip this file in favour of the other smaller ones in presentation.
import py_exec


a = "Original text"
b = a
print(f"a is now: {a}")
print(f"b is now: {b}")
print()


a = "New text"
print(f"a is now: {a}")
print(f"b is now: {b}")
print()


c = "erik.westrup@icloud.com"
d = c
print(f"c is now: {c}")
print(f"d is now: {d}")
print()


c = c.replace("@icloud.com", "@gmail.com")
print(f"c is now: {c}")
print(f"d is now: {d}")
print()


# Garbage collection (debug inspect)
e = "Text #1"
f = e
e = "Text #2"

f = "Text #3"
# "Text #1" is not gargabe collected

print(e, f)
