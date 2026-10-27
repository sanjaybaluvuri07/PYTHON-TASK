
# Progressive Water Tariff Analysis

households = []

n = int(input("Enter number of households: "))

FIXED_FEE = 100
EXCESS_LIMIT = 300

for i in range(n):
    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    units = float(input("Enter water consumption in units: "))
    late = input("Is payment late? (yes/no): ").lower()

    # Calculate progressive water charges
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5

    bill += FIXED_FEE

    # Late payment penalty
    penalty = 50 if late == "yes" else 0
    total = bill + penalty

    excessive = units > EXCESS_LIMIT

    households.append({
        "name": name,
        "units": units,
        "bill": bill,
        "penalty": penalty,
        "total": total,
        "excessive": excessive
    })

# Display household bills
print("\n------ WATER BILL REPORT ------")

for h in households:
    print("\nHousehold:", h["name"])
    print("Consumption:", h["units"], "units")
    print("Water charges + fixed fee: Rs.", round(h["bill"], 2))
    print("Penalty: Rs.", h["penalty"])
    print("Total bill: Rs.", round(h["total"], 2))

    if h["excessive"]:
        print("Warning: Excessive water usage!")
    else:
        print("Usage: Within the limit")

# Compare consumption patterns
if households:
    highest = max(households, key=lambda h: h["units"])
    lowest = min(households, key=lambda h: h["units"])
    average = sum(h["units"] for h in households) / len(households)

    print("\n------ CONSUMPTION ANALYSIS ------")
    print("Highest consumption:", highest["name"],
          "-", highest["units"], "units")
    print("Lowest consumption:", lowest["name"],
          "-", lowest["units"], "units")
    print("Average consumption:", round(average, 2), "units")
