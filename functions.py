import csv


def add_stock(file_name):
    print("Add ticker")
    ticker_name = input("Enter the ticker for your stock: ")
    with open(file_name, "a") as stock_file:
        writer = csv.writer(stock_file)
        writer.writerow([ticker_name, "False"])




def remove_stock():
    print("Remove stock")
    

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

