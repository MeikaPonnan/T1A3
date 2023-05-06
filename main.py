from colored import fg, bg, attr

from functions import add_stock, remove_stock, view_stock


print(f"{fg('blue')} {bg('white')} Welcome to your stock tracker {attr('reset')}")

file_name = "stocks.csv"

stocks = []
# check if file csv exists
try:
   stock_file = open(file_name, "r")

    #if it exists great
   stock_file.close()
   print("In try mode")

    #if it doesn't exist, then we create it
except FileNotFoundError as e:
    stock_file = open(file_name, "w")
    stock_file.write("Stocks,lists\n")
    stock_file.close()
    print("In except block")


def create_list():
    print("1. Enter '1' to add a new stock to your list")
    print("2. Enter '2' to search for a stock")
    print("3. Enter '3' to take out a stock from your list")
    print("4. Enter '4' to view your stock list")
    print("5. Enter '5' to view profit/loss on stocks")
    print("6. Enter '6' to edit a stock")
    print("7. Enter '7' to exit")
    choice = input("What do you want to do? ")
    return choice


user_input = ""

while user_input != "7":
    user_input = create_list()

    if (user_input == "1"):
        add_stock(file_name)
    elif (user_input == "2"):
        search_stock()
    elif (user_input == "3"):
        remove_stock(file_name)
    elif (user_input == "4"):
        view_stock(file_name)
    elif (user_input == "5"):
        calculate_stock()
    elif (user_input == "6"):
        edit_stock()
    elif (user_input == "7"):
        continue
    else:
        print("Invalid. Please choose from the list")

    input("Press Enter to continue.")


print("Thanks for your time!")
