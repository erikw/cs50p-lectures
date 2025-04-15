def get_age():
    while True:
        try:
            age = input("Please enter your age: "))
            age = int(age)
            return age

            # return int(input("Please enter your age: "))
        except ValueError:
            print("That is not a number. Please try again.")
        # calculate(age) # Can't have somethin after the except: to utilize the while-True retry.


def main():
    age = get_age()
    print(f"Your age is {age} years old.")

if __name__ == "__main__":
    main()
