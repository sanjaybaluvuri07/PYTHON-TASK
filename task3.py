
# Multi-Currency Travel Budget Analysis

def convert_to_base(amount, exchange_rate, fee_percent):
    """Convert an expense into the base currency, including fees."""
    converted_amount = amount * exchange_rate
    conversion_fee = converted_amount * fee_percent / 100
    total = converted_amount + conversion_fee

    return converted_amount, conversion_fee, total


def analyze_budget(expenses, exchange_rates, fee_percent, budget):
    """Analyze expenses, budget usage, and largest expense category."""
    category_totals = {}
    grand_total = 0.0

    print("\n========== TRAVEL EXPENSE REPORT ==========")
    print(
        f"{'Category':<16}{'Amount':>12}{'Currency':>12}"
        f"{'Converted':>14}{'Fee':>10}{'Total':>12}"
    )
    print("-" * 76)

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        currency = expense["currency"]

        if currency not in exchange_rates:
            raise ValueError(f"Missing exchange rate for {currency}")

        rate = exchange_rates[currency]

        converted, fee, total = convert_to_base(
            amount, rate, fee_percent
        )

        category_totals[category] = (
            category_totals.get(category, 0.0) + total
        )
        grand_total += total

        print(
            f"{category:<16}{amount:>12.2f}{currency:>12}"
            f"{converted:>14.2f}{fee:>10.2f}{total:>12.2f}"
        )

    print("-" * 76)
    print(f"Total travel expenses: Rs. {grand_total:.2f}")
    print(f"Travel budget:         Rs. {budget:.2f}")

    difference = budget - grand_total

    if difference > 0:
        print(f"Budget remaining:      Rs. {difference:.2f}")
        print(f"Budget used:           {grand_total / budget * 100:.2f}%")
    elif difference < 0:
        print(f"Budget exceeded by:    Rs. {-difference:.2f}")
        print(f"Budget used:           {grand_total / budget * 100:.2f}%")
    else:
        print("Budget status:         Exactly on budget")

    if category_totals:
        largest_category = max(category_totals, key=category_totals.get)
        largest_amount = category_totals[largest_category]

        print("\nExpense category summary:")
        for category, total in sorted(
            category_totals.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"{category:<20} Rs. {total:.2f}")

        print(f"\nLargest expense category: {largest_category}")
        print(f"Amount spent:             Rs. {largest_amount:.2f}")
        print(
            f"Share of total spending:  "
            f"{largest_amount / grand_total * 100:.2f}%"
            if grand_total > 0 else "Share of total spending:  0.00%"
        )


def main():
    print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

    # Base currency: INR (Indian Rupees)
    base_currency = "INR"

    # Example exchange rates: 1 foreign currency unit = INR value
    exchange_rates = {
        "INR": 1.0,
        "USD": 88.0,
        "EUR": 102.0,
        "GBP": 117.0,
        "JPY": 0.59
    }

    fee_percent = 2.0  # Example conversion fee: 2%

    # Example travel expenses
    expenses = [
        {"category": "Hotel", "amount": 300, "currency": "USD"},
        {"category": "Food", "amount": 100, "currency": "EUR"},
        {"category": "Transport", "amount": 50, "currency": "GBP"},
        {"category": "Shopping", "amount": 10000, "currency": "JPY"},
        {"category": "Activities", "amount": 5000, "currency": "INR"}
    ]

    try:
        budget = float(input("Enter total travel budget in INR: "))

        if budget <= 0:
            raise ValueError("Budget must be greater than zero.")

        analyze_budget(
            expenses,
            exchange_rates,
            fee_percent,
            budget
        )

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
