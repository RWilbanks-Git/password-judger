
import sys
import string
import pwinput
import re

def main():
    print("Hello!")
    start = input("Would you like me to judge your current password? (Yes/No)\n")

    if (start == "Yes"):
        warning = 0
        password = pwinput.pwinput(prompt = "Alright, enter the password in question.\n", mask = "*")
        checker(password, warning)

    elif (start == "No"):
        sys.exit("Ok, goodbye.")

    else:
        print("Invalid response. Please try again.\n\n")
        main()


def checker(password, warning):
    length = len(password)
    if (length <= 8):
        warning = warning + 1


    digitCount = sum(char.isdigit() for char in password)
    if (digitCount < 1):
        warning = warning + 1

    specialChar = r"[!@#$%^&*()_+{}\[\]:;<>,.?\\/-]"
    charsFound = re.findall(specialChar, password)
    charTotal = len(charsFound)

    if (charTotal < 1):
        warning = warning + 1
    else:
        warning = warning + 0

    result(length, digitCount, charTotal, warning)

def result(length, digitCount, charTotal, warning):
    if (warning == 0):
        print("Hey, your password looks pretty good!\n")
    else:
        print("\nHmmm... Your password seems to be missing something.\n\n")
        if (length <= 8):
            print("Your password seems a bit short.")
            print("Try to aim for at least 9 characters (if possible).\n")
        elif (digitCount < 1):
            print("Your password does not seem to have any digits.")
            print("Try adding in a number or two!\n")
        elif (charTotal < 1):
            print("You don't seem to have any special characters.")
            print("Try adding one in, like: '!', '?', '#', '+', etc.\n")
    restart()


def restart():
    again = input("\nWould you like to test out another password? (Yes/No)\n")
    if (again == "Yes"):
        print("\n")
        main()
    elif (again == "No"):
        sys.exit("\nOk, goodbye!")
    else:
        print("Invalid response. Please try again.\n\n")
        main()




if __name__ == "__main__":
    main()
