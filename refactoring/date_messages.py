MONTH_FMT = "Oh, you are born in month number {month}: 📅 {name}, known as the {alias}."

MONTHS_INFO = {
    1: {"name": "January", "alias": "Long Nights"},
    2: {"name": "February", "alias": "Snow Melt"},
    3: {"name": "March", "alias": "New Blossom"},
    4: {"name": "April", "alias": "Old Blossom"},
    5: {"name": "May", "alias": "Kord's Tempest"},
    6: {"name": "June", "alias": "Fresh Hay"},
    7: {"name": "July", "alias": "Pelor's Blessing"},
    8: {"name": "August", "alias": "Golden Harvest"},
    9: {"name": "September", "alias": "Pelor's Bounty"},
    10: {"name": "October", "alias": "Leaf Fall"},
    11: {"name": "November", "alias": "Sehanine"},
    12: {"name": "December", "alias": "Dark Frost"},
}

def message_header():
    balloons = "🎈" * 6
    return f"\n\n{balloons} Here is some birthday stats for you. {balloons}"

def message_for_year(year):
    if year <= 1950:
        return "👴 Wow, you are old now!"
    else:
        return "👶 You are still young, enjoy!"


def message_for_month(month):
    return MONTH_FMT.format(
        month=month, name=MONTHS_INFO[month]["name"], alias=MONTHS_INFO[month]["alias"]
    )


def message_for_day(day):
    msg = "Your birthday is "
    if day % 2 == 0:
        msg += "even"
    else:
        msg += "odd"
    return msg
