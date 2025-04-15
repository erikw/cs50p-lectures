"""
Demonstrate how Python interpreter walks thorough the file from top to end of execution.
"""

PI = 3.14159265359


def fix_casing(name):
    return name.capitalize()


def fix_name(name):
    name = name.strip()
    if name[0].islower():
        name = fix_casing(name)
    return name


def main():
    name = input("What's your name? ")
    name_fixed = fix_name(name)
    print(name_fixed)


if __name__ == "__main__":
    main()
