from colored import fg, bg, attr
import csv
import pandas


print(f"{fg('58')} {bg('118')} {attr('bold')} Welcome to your stock tracker {attr('reset')}")

file_name = "stocks.csv"

stocks = []

try:
   stock_file = open(file_name, "r")

   stock_file.close()
   print("In try block")

except FileNotFoundError as e:
    stock_file = open(file_name, "w")
    stock_file.write("Stocks,list\n")
    stock_file.close()
    print("In except block")


def add_stock():
    print("Add stock")
    stock = []
    stock.append(input("Enter the stock ticker: "))
    stock.append(int(input("Enter the number of shares bought: ")))
    stock.append(float(input("Enter the stock purchase price: ")))
    stock.append(float(input("Enter the stock selling price: ")))
    stocks.append(stock)
    save_data()


def search_stock():
    ticker = input("Enter the ticker for the stock you're looking for: ")
    found = False
    for stock in stocks:
        if stock[0].lower() == ticker.lower():
            view_stock(stock)
            found = True
        if not found:
            print(f"{fg('7')} {bg('9')} Stock not found. Please try again. {attr('reset')}")


def view_stock(stock):
    print("Ticker: " + stock[0])
    print("Shares: " + str(stock[1]))
    print("Purchase Price: " + str(stock[2]))
    print("Selling Price: " + str(stock[3]))
    print("Profit/Loss: " + str(calculate_profit_loss(stock)))
        

def view_stocks():
    for stock in stocks:
        view_stock(stock)
        print()

def save_data():
    with open(file_name, "w") as stock_file:
        writer = csv.writer(stock_file)
        writer.writerows(stocks)
    print(f"{fg('8')} {bg('129')} {attr('bold')} Stocks saved successfully. {attr('reset')}")


def remove_stock():
    print("Remove stock")
    ticker = input("Enter the stock you want to remove: ")
    found = False
    for stock in stocks:
        if stock[0].lower() == ticker.lower():
            stocks.remove(stock)
            save_data()
            found = True
    if not found:
        print(f"{fg('7')} {bg('9')} Stock not found. Please try again. {attr('reset')}")



def edit_stock():
    ticker = input("Enter the stock ticker your want to edit: ")
    found = False
    for stock in stocks:
        if stock[0].lower() == ticker.lower():
            print("Enter the changes for the stock: ")
            stock[1] = int(input("Enter the number of share bought: "))
            stock[2] = float(input("Enter the purchase price: "))
            stock[3] = float(input("Enter the selling price: "))
            save_data()
            found = True
    if not found:
        print(f"{fg('7')} {bg('9')} Stock not found. Please try again. {attr('reset')}")


def calculate_profit_loss(stock):
    shares_number = stock[1]
    purchase_price = stock[2]
    selling_price = stock[3]
    profit_loss = (selling_price - purchase_price) * shares_number
    return profit_loss



def create_list():
    print("1. Enter '1' to add a new stock to your list")
    print("2. Enter '2' to search for a stock")
    print("3. Enter '3' to take out a stock from your list")
    print("4. Enter '4' to view your stock list")
    print("5. Enter '5' to edit a stock")
    print("6. Enter '6' to exit")
    choice = input("What do you want to do? ")
    return choice



try:
   stock_file = open(file_name, "r")

   stock_file.close()
   print("In try block")

except FileNotFoundError as e:
    stock_file = open(file_name, "w")
    stock_file.write("Stocks,list\n")
    stock_file.close()
    print("In except block")

user_input = ""

while user_input != "6":
    user_input = create_list()

    if (user_input == "1"):
        add_stock()
    elif (user_input == "2"):
        search_stock()
    elif (user_input == "3"):
        remove_stock()
    elif (user_input == "4"):
        view_stocks()
    elif (user_input == "5"):
        edit_stock()
    elif (user_input == "6"):
        continue
    else:
        print(f"{bg('196')} {attr('bold')} Invalid. Please choose from the list {attr('reset')}")

    input(f"{fg('184')} Press Enter to continue. {attr('reset')}")


print(f"{bg('46')} {attr('blink')} Thanks for your time! {attr('reset')}")


