stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 700,
    "MSFT": 300
}


portfolio = {}

print("Enter your stock holdings (type 'done' to finish):")
while True:
    ticker = input("Stock ticker: ").upper()
    if ticker == "DONE":
        break
    if ticker not in stock_prices:
        print("Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"How many shares of {ticker}? "))
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
    except ValueError:
        print("Invalid number. Try again.")

total_value = 0
print("\nYour Portfolio Summary:")
for ticker, qty in portfolio.items():
    price = stock_prices[ticker]
    value = price * qty
    total_value += value
    print(f"{ticker}: {qty} shares × ${price} = ${value}")

print("\nTotal Investment Value:" ,{total_value})

save = input("Would you like to save the summary to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as f:
        f.write("Ticker,Shares,Price,Value\n")
        for ticker, qty in portfolio.items():
            price = stock_prices[ticker]
            value = price * qty
            f.write(f"{ticker},{qty},{price},{value}\n")
        f.write(f"\nTotal Investment Value,,,{total_value}\n")
    print(f"Portfolio saved to {filename}")
