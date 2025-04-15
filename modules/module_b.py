from module_a import bark_at

def main():
    name = "Swati"
    print(bark_at(name))




print(f"in module_b: {__name__}")
if __name__ == "__main__":
    main()
