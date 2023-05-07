import csv


def add_stock(file_name):
    print("Add stock")
    stock = []
    stock.append(input("Enter the stock ticker: "))
    stock.append(int(input("Enter the number of shares bought: ")))
    stock.append(float(input("Enter the stock purchase price: ")))
    stock.append(float(input("Enter the stock selling price: ")))
    stocks.append(stock)
    save_data()


def save_data(file_name):
    with open(file_name, "q", newline="") as s:
        writer = csv.writer(s)
        writer.writerows(stocks)


def search_stock(file_name):
    ticker = input("Enter the ticker for the stock you're looking for: ")
    found = False
    for stock in file_name:
        if stock[0].lower() == ticker.lower():
            view_stock(stock)
            found = True
        if not found:
            print("Stock" + ticker + "not found. Please try again.")

def remove_stock(file_name):
    print("Remove stock")
    stock_title = input("Enter the stock you want to remove: ")
    stock = []
    with open(file_name, "r") as stock_file:
        reader = csv.reader(stock_file)
        for row in reader:
            if (stock_title != row [0]):
                stock.append(row)
    print(stock)

    with open(file_name, "w") as stock_file:
        writer = csv.writer(stock_file)
        writer.writerows(stocks)




def view_stock(file_name):
    print("Ticker: " + stock[0])
    print("Shares: " + str(stock[1]))
    print("Purchase Price: " + str(stock[2]))
    print("Selling Price: " + str(stock[3]))
    print("Profit/Loss: " + str(calculate_profit_loss(stock)))


def view_stock():
    for stock in file_name:
        view_stock(stock)
        print()


