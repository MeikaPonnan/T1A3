from functions import add_stock, remove_stock, view_stock


print("Welcome to your stock tracker")

file_name = "list.csv"

def create_list():
    print("1. Enter '1' to add a new stock to your list")
    print("2. Enter '2' to take out a stock from your list")
    print("3. Enter '3' to view your stock list")
    print("4. Enter '4' to exit")
    choice = input("What do you want to do? ")
    return choice


user_input = ""

while user_input != "4":
    user_input = create_list()

    if (user_input == "1"):
        add_stock()
    elif (user_input == "2"):
        remove_stock()
    elif (user_input == "3"):
        view_stock()
    elif (user_input == "4"):
        continue
    else:
        print("Invalid. Please choose from the list")

    input("Press Enter to continue.")


print("Thanks for your time!")
