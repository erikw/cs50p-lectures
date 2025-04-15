"""
1. Show how exception traverses back the call stack.
2. Add try-except in main()
3. Add try-except in calculate(), show that this takes precedence.


**Call-stack in exceptions_3_functions.py (top-to-bottom)**
main()
    compute_prediction()
        calculate()
"""

PRODUCTION = True


def calculate(number):
    result = 10 / number
    result += 20
    return result


def compute_prediction(number):
    if PRODUCTION:
        return calculate(number)
    else:
        return number + 1


def main():
    nbr = int(input("Enter a number: "))
    res = compute_prediction(nbr)
    print(res)


if __name__ == "__main__":
    main()
