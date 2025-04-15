PI = 3.14159265359


def bark_at(person):
    print(f"🐕 Bark bark on you {person}!")


def main():
    name = input("What's your name? ")
    bark_at(name)


if __name__ == "__main__":
    main()
