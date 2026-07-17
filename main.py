import csv
prices = {
    "AAPL": 180,
    "GOOG": 2700,
    "TSLA": 250,
    "MSFT": 320,
    "AMZN": 130
}
portfolio = []
total = 0
while True:
    stock = input("Enter stock (or 'done'): ")

    if stock.lower() == "done":
        break

    stock = stock.upper()

    if stock not in prices:
        print("Invalid stock")
        continue

    try:
        qty = int(input("Enter quantity: "))
    except:
        print("Invalid quantity")
        continue

   
    found = False
    for i in range(len(portfolio)):
        if portfolio[i][0] == stock:
            portfolio[i] = (stock, portfolio[i][1] + qty)
            found = True
            break

    if not found:
        portfolio.append((stock, qty))

    total += prices[stock] * qty


print("\n----- Portfolio Summary -----")

for s, q in portfolio:
    value = prices[s] * q
    print(s, ":", q, "shares =", value)

print("Total Investment:", total)



with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Value"])

    for s, q in portfolio:
        writer.writerow([s, q, prices[s] * q])

    writer.writerow([])
    writer.writerow(["Total", "", total])