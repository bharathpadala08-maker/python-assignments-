
items = {
    "Idli": [20, 50],
    "Dosa": [40, 30],
    "Tea": [10, 40]
}

sales = 0

while True:
    print("\n--- Canteen Menu ---")
    for name, data in items.items():
        print(name, "- Rs.", data[0], "| Stock:", data[1])

    choice = input("Enter item name (or 'exit'): ")

    if choice.lower() == "exit":
        break

    if choice not in items:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")
    elif quantity > items[choice][1]:
        print("Insufficient stock!")
    else:
        bill = items[choice][0] * quantity
        items[choice][1] -= quantity
        sales += bill

        print("Order successful!")
        print("Bill amount: Rs.", bill)

print("\n--- Daily Sales Summary ---")
print("Total sales: Rs.", sales)

print("\n--- Remaining Stock ---")
for name, data in items.items():
    print(name, ":", data[1], "items")
