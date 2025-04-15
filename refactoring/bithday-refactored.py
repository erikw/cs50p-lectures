from date_validators import is_valid_year, is_valid_month, is_valid_day
from date_messages import message_header, message_for_year, message_for_month, message_for_day

import sys

QUESTION = "Hello dear user, please tell me what year, month and day were you born [yyyy-mm-dd] in. Then I will tell you something about it. Input: "


def read_birthday():
    while True:
        try:
            date = input(QUESTION)
            year, month, day = [int(p) for p in date.split("-")]
            break
        except ValueError as e:
            print("Try again. Input in format yyyy-mm-dd", file=sys.stderr)

    if not is_valid_year(year):
        raise ValueError("Invalid year range")

    if not is_valid_month(month):
        raise ValueError("Invalid month range")

    if not is_valid_day(day):
        raise ValueError("Invalid day range")

    return (year, month, day)


def main():
    year, month, day = read_birthday()

    print(message_header())
    print(message_for_year(year))
    print(message_for_month(month))
    print(message_for_day(day))


if __name__ == "__main__":
    main()
