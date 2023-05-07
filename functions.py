import csv


stocks = []

def add_stock(file_name):
    print("Add stock")
    stock = []
    stock.append(input("Enter the stock ticker: "))
    stock.append(int(input("Enter the number of shares bought: ")))
    stock.append(float(input("Enter the stock purchase price: ")))
    stock.append(float(input("Enter the stock selling price: ")))
    stocks.append(stock)
    save_data(file_name)


def save_data(file_name):
    with open(file_name, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(stocks)
    print("Stocks saved successfully.")

def load_data(file_name):
    try:
        with open(file_name, "r", newline = "") as f:
            reader = csv.reader(f)
            for row in reader:
                stocks.append(row)
    except FileNotFoundError:
        pass


def search_stock(file_name):
    ticker = input("Enter the ticker for the stock you're looking for: ")
    found = False
    for stock in stocks:
        if stock[0].lower() == ticker.lower():
            view_stock(stock)
            found = True
    if not found:
        print("Stock: " + ticker + " not found. Please try again.")

def remove_stock(file_name):
    print("Remove stock")
    ticker = input("Enter the stock you want to remove: ")
    found = False
    for stock in stocks:
        if stock[0].lower() == ticker.lower():
            stocks.remove(stock)
            save_data(file_name)
            found = True
    if not found:
        print("Stock: " + ticker + " not found. Please try again.")




def view_stock(file_name):
    print("Ticker: " + stock[0])
    print("Shares: " + str(stock[1]))
    print("Purchase Price: " + str(stock[2]))
    print("Selling Price: " + str(stock[3]))
    print("Profit/Loss: " + str(calculate_stock(stock)))


def view_stocks(file_name):
    for stock in stocks:
        view_stock(stock)
        print()

def calculate_profit_loss(file_name):
    shares_number = stock[1]
    purchase_price = stock[2]
    selling_price = stock[3]
    profit_loss = (selling_price - purchase_price) * shares_number
    return profit_loss

def edit_stock(file_name):
    ticker = input("Enter the stock ticker your want to edit: ")
    found = False
    for stock in stocks:
        if stock[0].lower() == ticker.lower():
            print("Enter the changes for the stock: ")
            stock[1] = int(input("Enter the number of share bought: "))
            stock[2] = float(input("Enter the purchase price: "))
            stock[3] = float(input("Enter the selling price: "))
            save_data(file_name)
            found = True
    if not found:
        print("Stock: " + ticker + " not found. Please try again. ")