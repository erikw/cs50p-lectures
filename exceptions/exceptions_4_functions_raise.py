import sys

PRODUCTION = True


def calculate(number):
    if number == 0: # Alternative to exception; check arguments being valid before using.
        raise ValueError("Calculation problem. Not possible to calcualte with number 0.")

    result = 10 / number
    result += 20
    return result


def compute_prediction(number):
    if PRODUCTION:
        return calculate(number)
    else:
        return number + 1


def main():
    try:
        nbr = int(input("Enter a number: "))
        res = compute_prediction(nbr)
    except ValueError as e:
        print(f"Caught error: {e}")
        sys.exit()

    print(res)


if __name__ == "__main__":
    main()
