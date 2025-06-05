# greeting.py

def main():
    name = input("Please enter your name: ")
    day = input("What day of the week is it today? ")
    print(f"Hello, {name}! Happy {day}!")

if __name__ == "__main__":
    main()
def get_feedback():
    feedback = input("What do you think about this greeting program? ")
    print("Thank you for your feedback!")

def main():
    name = input("Please enter your name: ")
    day = input("What day of the week is it today? ")
    print(f"Hello, {name}! Happy {day}!")
    get_feedback()

if __name__ == "__main__":
    main()