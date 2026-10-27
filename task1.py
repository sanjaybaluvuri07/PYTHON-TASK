
from dataclasses import dataclass

# Electricity tariff slabs (units, rate per unit)
SLABS = [
    (100, 2.00),
    (200, 3.50),
    (300, 5.00),
    (float("inf"), 7.00)
]

FIXED_CHARGE = 100.00
SURCHARGE_RATE = 0.05       # 5% surcharge
REBATE_RATE = 0.10          # 10% rebate if consumption <= 100 units
INCREASE_THRESHOLD = 0.30   # Flag bill increases above 30%


def calculate_energy_charge(units):
    """Calculate charges using progressive consumption slabs."""
    remaining = units
    energy_charge = 0
    previous_limit = 0

    for limit, rate in SLABS:
        slab_units = min(remaining, limit - previous_limit)
        energy_charge += slab_units * rate
        remaining -= slab_units
        previous_limit = limit

        if remaining <= 0:
            break

    return energy_charge


def calculate_bill(units):
    """Calculate the complete electricity bill."""
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    energy_charge = calculate_energy_charge(units)
    subtotal = energy_charge + FIXED_CHARGE
    surcharge = subtotal * SURCHARGE_RATE

    rebate = 0
    if units <= 100:
        rebate = energy_charge * REBATE_RATE

    total_bill = subtotal + surcharge - rebate

    return {
        "units": units,
        "energy_charge": energy_charge,
        "fixed_charge": FIXED_CHARGE,
        "surcharge": surcharge,
        "rebate": rebate,
        "total": total_bill
    }


def compare_months(monthly_usage):
    """Compare monthly bills and flag unusual increases."""
    previous_bill = None

    print("\nMONTHLY ELECTRICITY BILL REPORT")
    print("-" * 90)
    print(
        f"{'Month':<12}{'Units':>8}{'Energy':>12}"
        f"{'Surcharge':>12}{'Rebate':>10}{'Total':>12}"
        f"  Status"
    )
    print("-" * 90)

    bills = []

    for month, units in monthly_usage.items():
        bill = calculate_bill(units)
        bills.append((month, bill))

        status = "Normal"
        if previous_bill is not None:
            increase = bill["total"] - previous_bill
            percentage = increase / previous_bill if previous_bill else 0

            if percentage > INCREASE_THRESHOLD:
                status = f"ALERT (+{percentage:.1%})"
            elif increase > 0:
                status = f"+{percentage:.1%}"
            elif increase < 0:
                status = f"{percentage:.1%}"

        print(
            f"{month:<12}{units:>8.0f}"
            f"{bill['energy_charge']:>12.2f}"
            f"{bill['surcharge']:>12.2f}"
            f"{bill['rebate']:>10.2f}"
            f"{bill['total']:>12.2f}  {status}"
        )

        previous_bill = bill["total"]

    print("-" * 90)

    if bills:
        average = sum(b["total"] for _, b in bills) / len(bills)
        print(f"Average monthly bill: Rs. {average:.2f}")

        highest_month, highest_bill = max(
            bills, key=lambda item: item[1]["total"]
        )
        print(
            f"Highest bill: {highest_month} "
            f"(Rs. {highest_bill['total']:.2f})"
        )


# Main program
if __name__ == "__main__":
    print("PROGRESSIVE ELECTRICITY BILLING SYSTEM")

    monthly_usage = {}

    try:
        count = int(input("Enter number of months to compare: "))

        if count <= 0:
            raise ValueError("Number of months must be positive.")

        for i in range(count):
            month = input(f"Enter month {i + 1} (e.g., January): ").strip()

            if not month or month in monthly_usage:
                raise ValueError("Month must be nonempty and unique.")

            units = float(input(f"Enter units consumed in {month}: "))

            if units < 0:
                raise ValueError("Units cannot be negative.")

            monthly_usage[month] = units

        compare_months(monthly_usage)

    except ValueError as error:
        print("Input error:", error)
