import os

FILENAME = "portfolio.txt"

def add_stock():
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    try:
        shares = float(input(f"How many shares of {ticker} do you own? "))
        price = float(input(f"What is the current price of {ticker}? "))
        
        # Open file in 'append' mode
        with open(FILENAME, "a") as f:
            f.write(f"{ticker},{shares},{price}\n")
        print(f"Successfully added {ticker} to your portfolio.\n")
    except ValueError:
        print("Invalid input. Please use numbers for shares and price.")

def calculate_total():
    if not os.path.exists(FILENAME):
        print("No portfolio found. Add some stocks first!")
        return

    total_value = 0
    print("\n--- Current Portfolio ---")
    
    with open(FILENAME, "r") as f:
        for line in f:
            # Basic string parsing
            ticker, shares, price = line.strip().split(",")
            investment = float(shares) * float(price)
            total_value += investment
            print(f"{ticker}: {shares} shares @ ${price} = ${investment:,.2f}")
    
    print("-" * 25)
    print(f"Total Investment: ${total_value:,.2f}\n")

def main():
    while True:
        print("1. Add Stock")
        print("2. View Portfolio & Total")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            calculate_total()
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()