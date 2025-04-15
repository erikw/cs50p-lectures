PI = 3.14159265359


def bark_at(person):
    return f"🐕 Bark bark on you {person}!"


def main():
    name = input("What's your name? ")
    print(bark_at(name))


if __name__ == "__main__":
    main()
