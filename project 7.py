
areas = ["Area A", "Area B", "Area C"]
days = int(input("Enter number of days: "))

demand = []
supply = []

for area in areas:
    print("\n", area)
    d = float(input("Enter daily water demand (litres): "))
    demand.append(d)

    readings = []
    for day in range(days):
        water = float(input("Day " + str(day + 1) + " supply: "))
        readings.append(water)

    supply.append(readings)

print("\n--- Water Distribution Report ---")

shortages = []

for i in range(len(areas)):
    total_supply = sum(supply[i])
    total_demand = demand[i] * days
    shortage = max(0, total_demand - total_supply)
    shortages.append(shortage)

    print("\n", areas[i])
    print("Total demand:", total_demand, "litres")
    print("Total supply:", total_supply, "litres")
    print("Total shortage:", shortage, "litres")

    if total_demand > 0:
        print("Supply percentage:",
              round(total_supply / total_demand * 100, 2), "%")

most_underserved = areas[shortages.index(max(shortages))]

print("\nMost underserved area:", most_underserved)
