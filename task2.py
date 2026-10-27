
# Hospital Billing and Patient Classification System

# Sample billing rates (in rupees)
CONSULTATION_FEE = 500.00
DIAGNOSTIC_FEE = 1000.00
TREATMENT_FEE = 2000.00

# Sample concession policy
SENIOR_CITIZEN_AGE = 60
SENIOR_CONCESSION = 10       # 10% discount
HIGH_BILL_THRESHOLD = 5000.00
HIGH_BILL_CONCESSION = 5     # 5% discount

# Sample payment classification policy
PAYMENT_POLICIES = {
    "FULL": (80, "Full Payment"),
    "PARTIAL": (40, "Partial Payment"),
    "LOW": (0, "Low Payment Capacity")
}


def get_valid_amount(prompt):
    """Read and validate a non-negative payment amount."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")


def calculate_charges(consultation, diagnostic, treatment):
    """Calculate total hospital charges."""
    return consultation + diagnostic + treatment


def apply_concessions(total, age):
    """Apply eligible concessions to the hospital bill."""
    discount = 0.0
    reasons = []

    if age >= SENIOR_CITIZEN_AGE:
        discount += total * SENIOR_CONCESSION / 100
        reasons.append(f"Senior citizen concession: {SENIOR_CONCESSION}%")

    # Apply the high-bill concession to the original bill.
    # Discounts are additive and cannot exceed the original total.
    if total >= HIGH_BILL_THRESHOLD:
        discount += total * HIGH_BILL_CONCESSION / 100
        reasons.append(f"High bill concession: {HIGH_BILL_CONCESSION}%")

    discount = min(discount, total)
    return discount, reasons


def classify_patient(total_bill, amount_paid):
    """Classify payment capacity using the sample policy."""
    if total_bill == 0:
        return "No Payment Due"

    payment_percentage = (amount_paid / total_bill) * 100

    if payment_percentage > 100:
        return "Overpayment - Verify Refund"

    for threshold, category in PAYMENT_POLICIES.values():
        if payment_percentage >= threshold:
            return category

    return "Low Payment Capacity"


def generate_bill():
    """Collect patient details, validate inputs, and print the bill."""
    print("\n========== HOSPITAL BILLING SYSTEM ==========")

    patient_name = input("Enter patient name: ").strip()
    if not patient_name:
        print("Patient name cannot be empty.")
        return

    while True:
        try:
            age = int(input("Enter patient age: "))
            if age < 0 or age > 130:
                print("Enter an age between 0 and 130.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number for age.")

    print("\nEnter service charges (in Rs.):")
    consultation = get_valid_amount("Consultation charge: ")
    diagnostic = get_valid_amount("Diagnostic charge: ")
    treatment = get_valid_amount("Treatment charge: ")

    # Calculate bill
    gross_total = calculate_charges(
        consultation, diagnostic, treatment
    )

    discount, reasons = apply_concessions(gross_total, age)
    net_bill = gross_total - discount

    print("\n========== BILL SUMMARY ==========")
    print(f"Patient Name       : {patient_name}")
    print(f"Patient Age        : {age}")
    print(f"Consultation       : Rs. {consultation:.2f}")
    print(f"Diagnostic         : Rs. {diagnostic:.2f}")
    print(f"Treatment          : Rs. {treatment:.2f}")
    print("----------------------------------")
    print(f"Gross Bill         : Rs. {gross_total:.2f}")
    print(f"Total Concession   : Rs. {discount:.2f}")

    if reasons:
        for reason in reasons:
            print(f"  - {reason}")
    else:
        print("Concession Reason  : None")

    print(f"Net Bill           : Rs. {net_bill:.2f}")

    amount_paid = get_valid_amount("\nEnter amount paid (Rs.): ")

    if amount_paid > net_bill:
        balance = 0.0
        outstanding = 0.0
        refund_due = amount_paid - net_bill
    else:
        balance = net_bill - amount_paid
        outstanding = balance
        refund_due = 0.0

    classification = classify_patient(net_bill, amount_paid)

    print("\n========== PAYMENT DETAILS ==========")
    print(f"Amount Paid        : Rs. {amount_paid:.2f}")
    print(f"Outstanding Balance: Rs. {outstanding:.2f}")
    print(f"Refund Due         : Rs. {refund_due:.2f}")
    print(f"Patient Category   : {classification}")
    print("=====================================")


if __name__ == "__main__":
    generate_bill()
