
appliances = ["Fan", "Light", "TV"]
days = 7
matrix = []

limit = float(input("Enter daily consumption limit (units): "))

for appliance in appliances:
    readings = []
    print("\nEnter daily units for", appliance)

    for day in range(days):
        units = float(input("Day " + str(day + 1) + ": "))
        readings.append(units)

    matrix.append(readings)

print("\n--- Weekly Consumption Matrix ---")

for i in range(len(appliances)):
    total = sum(matrix[i])
    print(appliances[i], "total:", total, "units")

print("\n--- Daily Totals ---")

for day in range(days):
    total = 0

    for i in range(len(appliances)):
        total += matrix[i][day]

    print("Day", day + 1, ":", total, "units")

    if total > limit:
        print("Warning: Consumption exceeds limit!")

print("\n--- Weekly Total ---")
print(sum(sum(row) for row in matrix), "units")
