import sys

while True:
    try:
        date = input("Hello dear user, please tell me what year, month and day were you born [yyyy-mm-dd] in. Then I will tell you something about it. Input: ")
        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        break
    except ValueError as e:
        print("Try again. Input in format yyyy-mm-dd", file=sys.stderr)

if not (0 <= year <= 9999):
    raise ValueError("Invalid year range")

if not (1 <= month <= 12):
    raise ValueError("Invalid month range")

if not (1 <= day <= 31):
    raise ValueError("Invalid day range")

print()
print("🎈🎈🎈🎈🎈🎈 Here is some birthday stats for you. 🎈🎈🎈🎈🎈🎈")

if year <= 1950:
    print("👴 Wow, you are old now!")
else:
    print("👶 You are still young, enjoy!")


print(f"Oh, you are born in month number {month}: ", end="")
match month:
    case 1:
        print("📅 January, known as the Long Nights.")
    case 2:
        print("📅 February, known as the Snow Melt.")
    case 3:
        print("📅 March, known as the New Blossom.")
    case 4:
        print("📅 April, known as the Old Blossom.")
    case 5:
        print("📅 May, known as the Kord's Tempest.")
    case 6:
        print("📅 June, known as the Fresh Hay.")
    case 7:
        print("📅 July, known as the Pelor's Blessing.")
    case 8:
        print("📅 August, known as the Golden Harvest.")
    case 9:
        print("📅 September, known as the Pelor's Bounty.")
    case 10:
        print("📅 October, known as the Leaf Fall.")
    case 11:
        print("📅 November, known as the Sehanine.")
    case 12:
        print("📅 December, known as the Dark Frost.")

if day % 2 == 0:
    print("Your bith-day is even.")
else:
    print("Your bith-day is odd.")
