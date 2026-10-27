
# Traffic Violation Penalty Calculator

fine_rules = {
    "Car": {
        "Overspeeding": 1000,
        "No Helmet": 0,
        "Signal Jumping": 1000,
        "Drunk Driving": 10000
    },
    "Bike": {
        "Overspeeding": 1000,
        "No Helmet": 500,
        "Signal Jumping": 1000,
        "Drunk Driving": 10000
    },
    "Truck": {
        "Overspeeding": 2000,
        "No Helmet": 0,
        "Signal Jumping": 2000,
        "Drunk Driving": 10000
    }
}

total_penalty = 0
disqualified = False

n = int(input("Enter number of violations: "))

for i in range(n):
    print("\nViolation", i + 1)

    vehicle = input("Vehicle category (Car/Bike/Truck): ").title()
    offence = input(
        "Offence (Overspeeding/No Helmet/Signal Jumping/Drunk Driving): "
    ).title()
    repeat = input("Is it a repeat offence? (yes/no): ").lower()

    if vehicle not in fine_rules or offence not in fine_rules[vehicle]:
        print("Invalid vehicle category or offence.")
        continue

    fine = fine_rules[vehicle][offence]

    # Repeat offence: additional 50% fine
    if repeat == "yes":
        fine = fine * 1.5

    # Disqualification condition (example rule)
    if offence == "Drunk Driving" and repeat == "yes":
        disqualified = True

    total_penalty += fine

    print("Fine for this violation: Rs.", fine)

print("\n------ FINAL REPORT ------")
print("Total penalty: Rs.", total_penalty)

if disqualified:
    print("Status: Disqualification condition identified.")
else:
    print("Status: No disqualification condition identified.")

print("Note: Fine amounts and disqualification rules are illustrative.")
