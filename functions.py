import csv


def add_stock(file_name):
    print("Add stock")
    stock = []
    stock.append(input("Enter the stock ticker: "))
    stock.append(int(input("Enter the number of shares bought: ")))
    stock.append(float(input("Enter the stock purchase price: ")))
    stock.append(float(input("Enter the stock selling price: ")))
    #stocks.append(stock)
    #save_data()

    #ticker_name = input("Enter the ticker for your stock: ")
    #with open(file_name, "a") as stock_file:
       # writer = csv.writer(stock_file)
        #writer.writerow([ticker_name, "False"])

def save_data():
    with open(file_name, "q", newline="") as s:
        writer = csv.writer(s)
        writer.writerows(stocks)

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
    print("View stock list")
    with open(file_name, "r") as stock_file:
        reader = csv.reader(stock_file)
        reader.__next__()
        for row in reader:
            if(row[1] == "True"):
                print(f"Stock: {row[0]}")
            else:
                print(f"Add stock to continue")

