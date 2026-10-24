def inventory_transfer_system():
    # 1. Define branch data (Current stock vs. Goal/Target stock)
    # We will look at a single item: "Laptops"
    branches = {
        "Store A": {"current": 25, "target": 10},  # Has a surplus of 15
        "Store B": {"current": 3, "target": 12},  # Needs 9
        "Store C": {"current": 5, "target": 15}  # Needs 10
    }

    # Rule/Constraint: Maximum units allowed in a single transfer order
    max_transfer_limit = 8

    # Lists to keep track of stores with extra stock vs stores that need stock
    surplus_stores = []
    shortage_stores = []

    # Step 2: Calculate who has surplus and who has shortage
    for name, data in branches.items():
        difference = data["current"] - data["target"]

        if difference > 0:
            surplus_stores.append({"store": name, "qty": difference})
        elif difference < 0:
            # Use abs() to make the shortage a positive number
            shortage_stores.append({"store": name, "qty": abs(difference)})

    # Step 3: Generate the transfer orders
    transfer_orders = []

    s_index = 0  # Index for surplus stores
    h_index = 0  # Index for shortage stores

    while s_index < len(surplus_stores) and h_index < len(shortage_stores):
        supplier = surplus_stores[s_index]
        receiver = shortage_stores[h_index]

        # Find the transfer amount based on what's available, needed, and the max limit rule
        amount_to_transfer = min(supplier["qty"], receiver["qty"], max_transfer_limit)

        if amount_to_transfer > 0:
            transfer_orders.append({
                "from": supplier["store"],
                "to": receiver["store"],
                "quantity": amount_to_transfer
            })

            # Reduce the remaining quantities
            supplier["qty"] -= amount_to_transfer
            receiver["qty"] -= amount_to_transfer

        # Move to the next store if current one is finished
        if supplier["qty"] == 0:
            s_index += 1
        if receiver["qty"] == 0:
            h_index += 1

    # Step 4: Print the final report
    print("=" * 45)
    print("RETAIL INVENTORY TRANSFER REPORT")
    print(f"Constraint: Max {max_transfer_limit} units per transfer")
    print("=" * 45)

    for order in transfer_orders:
        print(f"• Move **{order['quantity']}** units from **{order['from']}** ➔ **{order['to']}**")


# Run the program
if __name__ == "__main__":
    inventory_transfer_system()